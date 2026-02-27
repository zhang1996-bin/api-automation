import docx

def read_docx_file(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"读取文档时出错: {str(e)}"

if __name__ == "__main__":
    doc_path = "接口自动化文档.docx"
    content = read_docx_file(doc_path)
    print("文档内容:")
    print(content)
