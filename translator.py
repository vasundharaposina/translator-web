from deep_translator import GoogleTranslator

def context_translate(text, target_language, context=""):
    try:
        return GoogleTranslator(
            source='auto',
            target=target_language.lower()
        ).translate(text)
    except Exception as e:
        return f"Error: {e}"