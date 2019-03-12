# Intervocalic-t-Search
GOAL: A program which takes a .txt file as it’s input, searches for all “intervocalic /t/” words, and extracts them into an .csv file.

(1)	Take .txt input:
  There are multiple .txt files for each recording session. The program can do one at a time, I’d don’t mind having them in separate excel sheets.
  The .txt files are transcriptions of the recordings in the following format:
  M001   how was the little school today ? . 
         00:05:34.203 – 00:05:42.211

  G001   we went to the /park for gym time/
         00:05:42.307 – 00:05:48.001

  B001   /it was okay/ {unclear} . [chews food]
         00:05:44.829 – 00:05:54.395
  All transcriptions will be in lower case, with no capitals except for proper nouns and “I”. Other symbols which are frequency used in transcriptions include /, [], {}, ., ?.


(2)	Read .txt file:
  Search the file for any words which contain the following character sets:
      VtV
      VttV
      Vtle
      Vttle
      ightV
      Vt’
      ight'
      Where V = a, e, i, o, u, y
  Note that some segments may have more than one intervocalic /t/

  All text within [] or {} brackets must be ignored and not included in the excel sheet

  If possible (although not necessary):
  Count words with two of the above character sets only once (i.e. competitors)
  And don’t count Vtion words (position)
  But count it if it has correct set (i.e. competition)
  Note the starting time and/or speaker of the segment in which the /t/ occur
(3)	Output an excel file:
  If the time and speaker can’t/isn’t going to be noted with the word, then the program can output either:
  1.	A list of all intervocalic /t/ words said, multiple occurrences of a word can be rewritten
  little
  pretend
  attack
  pretend
  attack
  i.e.




  2.	Each word of intervocalic /t/ which occurred in the recording, with a number next to it indicating the total frequency of the word within the input .txt
  little	1
  pretend	2
  attack	2
  i.e. 

  If the time and speaker of each word is included in the output, please include that data next to each word (order isn’t important as long as it’s kept consistent).
