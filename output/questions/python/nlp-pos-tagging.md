# POS Tagging #1

- **Domain:** python
- **Difficulty:** Medium
- **Max Score:** 10
- **Success Ratio:** 0.7710760795065114
- **Total Submissions:** 1459
- **Solved Count:** 1125
- **URL:** https://www.hackerrank.com/challenges/nlp-pos-tagging

## Problem Statement

You are provided with the POS-tagged version of a sentence. The tags that are used are the most commonly used standard from the Pen Tree Tagset. 

Your task is to fill in the missing tags which have been replaced by question marks.
The missing tags will be restricted to the set of tags which you already see in the POS tagged version of this sentence. <br>
If there are two question marks (??), it indicates a 2-letter tag (CC, JJ, NN etc.). <br>
If there are three question marks (???), it indicates a 3-letter tag (NNP, PPS, VBP).  


	The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/?? ,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/?? that/IN never/RB caught/??? fire/NN ./.
    
In the plain-text box below, submit the sentence, as is, with only the question marks filled in appropriately and nothing else changed.  

For example, your answer may look like this (This is **not** the correct answer): 

	The/DT planet/NN Jupiter/NNP and/CC its/PPS moons/NNS are/VBP in/IN effect/NN a/DT minisolar/JJ system/CC ,/, and/CC Jupiter/NNP itself/PRP is/VBZ often/RB called/VBN a/DT star/CC that/IN never/RB caught/NNP fire/NN ./.
