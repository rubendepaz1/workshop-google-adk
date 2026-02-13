import os
import logging
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from dotenv import load_dotenv
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# ==========================================
# 🛠️ CUSTOM TOOLS
# ==========================================

def publish_to_web(content: str) -> str:
    """
    Publishes the final content to the public website UI.
    CRITICAL: This tool must ONLY be called after explicit user approval.

    Args:
        content (str): The markdown content to publish.
    """
    print(f"\n[SYSTEM ACTION] 🚀 Sending to Public Web...")

    web_url = os.environ.get("PUBLIC_WEB_URL")

    if not web_url:
        return "❌ ERROR: No PUBLIC_WEB_URL configured."

    try:
        response = requests.post(
            f"{web_url}/api/publish",
            json={"content": content},
            timeout=10
        )

        if response.status_code == 200:
            return f"✅ SUCCESS: Published! View it at: {web_url}"
        else:
            return f"❌ ERROR: Web returned {response.status_code}"

    except Exception as e:
        return f"❌ ERROR: Connection failed: {str(e)}"

# ==========================================
# 🤖 POWERLIFTING AGENT (Coachy)
# ==========================================

coachy_agent = LlmAgent(
    model="gemini-2.0-flash-001",
    name="coachy",
    description="Specialist in powerlifting news and the Momentum Coach app.",
    instruction=(
        "Eres Coachy, un experto en powerlifting y en la app momentumcoach.es.\n"
        "Tu objetivo es informar sobre noticias de powerlifting y detalles de la app Momentum Coach.\n"
        "REGLAS CRÍTICAS:\n"
        "1. SIEMPRE debes empezar tus respuestas con 'hola soy Coachy'.\n"
        "2. Usa 'google_search' para buscar las últimas noticias de powerlifting o información sobre momentumcoach.es.\n"
        "3. Mantén un tono motivador y experto.\n"
        "4. Si te preguntan algo que no sabes, búscalo en internet.\n"
        "5. Tienes una herramienta 'publish_to_web' para publicar contenido en la web pública.\n"
        "6. Cuando el usuario te pida publicar, redacta el contenido en Markdown y usa 'publish_to_web' para enviarlo."
    ),
    tools=[google_search, publish_to_web]
)

# --- ADK ENTRY POINT ---
root_agent = coachy_agent
