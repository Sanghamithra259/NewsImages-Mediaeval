def build_prompt(title, tags):
    tags_str = ', '.join(tags.split(';'))
    return f"{title}. Keywords: {tags_str}"
