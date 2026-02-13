import os
import logging
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

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
        "4. Si te preguntan algo que no sabes, búscalo en internet."
    ),
    tools=[google_search]
)

# --- ADK ENTRY POINT ---
root_agent = coachy_agent
