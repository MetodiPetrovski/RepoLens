def chunk_to_text(chunk):
    parts = []

    parts.append(f"Function: {chunk['qualified_name']}")

    if chunk.get("class_name"):
        parts.append(f"Class: {chunk['class_name']}")

    parts.append(f"File: {chunk['file']}")

    if chunk.get("args"):
        parts.append("Parameters: " + ", ".join(chunk["args"]))

    if chunk.get("docstring"):
        parts.append("Description: " + chunk["docstring"])

    if chunk.get("calls"):
        parts.append("Calls: " + ", ".join(chunk["calls"]))

    # IMPORTANT: keep code, but separate clearly
    if chunk.get("source"):
        parts.append("Implementation:\n" + chunk["source"])

    return "\n\n".join(parts)
