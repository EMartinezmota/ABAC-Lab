import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from core.myabac import parse_abac_file
from acl_analyzer import compare_acl
from acl_generator import generate_acl
from api_functions.gemini_call import gemini_api_call
from helper_functions import append_from_file , clear_file, write_to_file


def main():
 
    user, res, rule = parse_abac_file("DATASETS/abac-datasets/healthcare.abac")
    generate_acl(user, res, rule, "llm-research/generated-ACL/healthcare-ACL.txt")
    # user, res, rule = parse_abac_file("DATASETS/abac-datasets/project-management.abac")
    # generate_acl(user, res, rule)
    # user, res, rule = parse_abac_file("DATASETS/abac-datasets/university.abac")
    # generate_acl(user, res, rule)
    # user, res, rule = parse_abac_file("DATASETS/abac-datasets/workforce.abac")
    # generate_acl(user, res, rule)
    # user, res, rule = parse_abac_file("DATASETS/abac-datasets/edocument.abac")
    # generate_acl(user, res, rule)
   
    # temp_text = compare_acl("llm-research/generated-ACL/healthcare-ACL.txt", "llm-research/generated-ACL/healthcare-ACL.txt")
    # write_to_file("llm-research/generated-ACL/delete.txt", temp_text)
    
    abac_rules_generated = "llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-ABAC-rules.txt"
    acl_file = "llm-research/generated-ACL/healthcare-ACL.txt"
    attribute_data_file = "DATASETS-for-LLM/healthcare/healthcare.abac"
    attribute_description_file ="DATASETS-for-LLM/healthcare/README.md"
    
    gemini_api_call(abac_rules_generated, acl_file, attribute_data_file, attribute_description_file)

    dst = "llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-healthcare.abac"
    src = "DATASETS-for-LLM/healthcare/healthcare.abac"
    clear_file(dst)
    append_from_file(dst, src)
    src = "llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-ABAC-rules.txt"
    append_from_file(dst, src)

    user2, res2, rule2 = parse_abac_file("llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-healthcare.abac")
    generate_acl(user2, res2, rule2, "llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-ACL.txt")


    temp_text = compare_acl(acl_file, "llm-research/llm-generated-data/gemini/gemini-healthcare/gemini-ACL.txt")
    write_to_file("llm-research/llm-generated-data/gemini/gemini-healthcare/gemini.log", temp_text)




if __name__ == "__main__":
    main()
