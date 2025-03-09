import json

def generate_combined_pose(sentence):
    isl_sentence = rearrange_to_isl(sentence)
    words = isl_sentence.split()
    
    final_pose_sequence = {"frames": []}
    
    for word in words:
        if word in word_to_pose:
            with open(word_to_pose[word], "r") as f:
                pose_data = json.load(f)
                final_pose_sequence["frames"].extend(pose_data["frames"])

    return final_pose_sequence
