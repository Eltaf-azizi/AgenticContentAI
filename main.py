from agents.research_agent import research_topic
from agents.outline_agent import generate_outline
from agents.writer_agent import write_draft
from agents.editor_agent import edit_content
from agents.image_agent import generate_image


def main():
    print("🚀 Welcome to AgenticX - AI-Powered content Creator")
    topic = input("🔍 Enter your content topic or brief: ")


    print("\n📚 Researching...")
    background = research_topic(topic)
    print("\n🔍 Background Info:\n", background)


    print("\n🧠 Generating Outline...")
    outline = generate_outline(topic, background)
    print("\n📝 Content Outline:\n", outline)


    print("\n✍️ Writting First Draft...")
    draft = write_draft(topic, outline)
    print("\n📄 Content Draft:\n", draft)


    print("\n🖌️ Editting & Optimizing...")
    final_content = edit_content(draft)
    print("\n✅ Final Edited Content:\n", final_content)


    print("\n🖼️ Generating Visual...")
    image_url = generate_image(topic)
    print("\n🌄 Image URL:\n", image_url)



if __name__ == "__main__":
    main()