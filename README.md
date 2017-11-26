#markov

The end goal is to host a website that plays procedurally generated music.

Short term goals:
Clean out this repository...It's a mess.
There's an API called "Mingus" that solves a lot of problems.
Right now my probability matrix only accounts for the note right after.
  What if I made probability matrices for 2 notes after current, 3 notes after current, etc.
  

Long term things to think about:
  How do I incorporate harmony?
  


Logs
11/26/17: Turned adjacency matrix into probability matrix. Wrote basic note-generating algorithm. 
   Some glaring issues...
      Phrases all begin and end on the same note.
      Notes are too random.
