#Functions to assist in the llm-research folder .py files
#includes but is not limmited to files to open text files
# combine text files


def write_to_file(filename, lines=None):

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line+"\n")
    
    return


def clear_file(filename):
    with open(filename,"w", encoding="utf-8"):
        pass

    return


def read_entire_file(filename):
    
    with open (filename, "r", encoding="utf-8") as f:
        return f.read().strip()
    
    return

#removed all calls, I just copied the data set and removed the rules.
def read_until_marker(filename, stop_marker):
    lines = []
    with open (filename, "r", encoding="utf-8" ) as f:
        for line in f:
            if line.strip() == stop_marker:
                break
            lines.append(line.rstrip())
        return "\n".join(lines).strip()

def append_to_file(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(str(text) + "\n")

def append_from_file(dest_file, src_file):
    with open(src_file, "r", encoding="utf-8") as src:
        content = src.read()
    with open(dest_file, "a", encoding="utf-8") as dst:
        dst.write(content)

def prompt_generator(acl_file, attribute_data_file, attribute_description_file, complete_request_file ):
   
    prompt_file = "llm-research/engineered-prompt.txt"

    # read inputs
    try:
        prompt = read_entire_file(prompt_file)
        acl = read_entire_file(acl_file)
        attribute_data = read_entire_file(attribute_data_file)
        attribute_description = read_entire_file(attribute_description_file)

    except FileNotFoundError as e:
        print(f"Error reading file: {e}")
        return
    except Exception as e:
        print(f"Unexpected read error: {e}")
        return

    # build a single request file
    sections = [
        ("NEW REQUEST", prompt),
        ("ATTRIBUTE_DESCRIPTION", attribute_description),
        ("ATTRIBUTE_DATA", attribute_data),
        ("ACL", acl)
    ]

    combined = []

    for title, content in sections:
        combined.append(f"Section: {title}\n{content}  ##\n")

    write_to_file(complete_request_file, combined)

    
    # combined_text = "\n".join(combined).strip()

    # with open(output_path, "w", encoding="utf-8") as out:
    #     out.write(combined_text + "\n")
