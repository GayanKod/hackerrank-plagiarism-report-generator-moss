# Plagiarism Report Generator for Hackerrank based Coding Contests

This is a simple command-line Python program designed to generate plagiarism reports for contestant-submitted codes in Hackerrank-based contests.

With this tool, you can easily identify whether contestants have copied or shared code among each other.

The tool utilizes a robust code plagiarism detection algorithm developed by Stanford University, known as ‘Moss’.

## What is Moss?**

Moss (for a Measure Of Software Similarity) is an automatic system for determining the similarity of programs. To date, the main application of Moss has been in detecting plagiarism in programming classes. Since its development in 1994, Moss has been very effective in this role. The algorithm behind moss is a significant improvement over other cheating detection algorithms (at least, over those known to us).
(Source: https://theory.stanford.edu/~aiken/moss/)

## How to use this tool?

I recommend you to use Linux based OS to run this code. 

**Step 1:** You need to download all the codes submitted by the contestants for each question and save to local machine with the following hierarchy

```bash
out/2020-03-01-06-01
├── a-walk-to-remember-1
│   ├── c
│   │   ├── Cygnus_UOK.c
│   │   ├── KingCoders_SEUSL.c
│   │   └── StackTrace_NSBM_.c
│   ├── cpp
│   │   ├── BlackHawks_USJ.cpp
│   │   ├── Code_Clan_RUSL.cpp
│   │   ├── Cyborgs_USJ.cpp
│   │   ├── FRIDAY_USJ.cpp
│   │   ├── JPAC_UOP.cpp
│   │   ├── Paradox_UOJ.cpp
│   │   └── XCODERS_UOP.cpp
│   ├── csharp
│   │   └── CodeMart_UOR.cs
```

To do that, I recommend using this tool available on GitHub: https://github.com/kasvith/hackerrank-dl

**Step 2:** You need to register with Moss and obtain a Moss Registered USER_ID.

This USER_ID is required for the program. Once you have the USER_ID, replace the code’s USER_ID line with your USER_ID.

**To Register to the Moss,**
you need to visit: https://theory.stanford.edu/~aiken/moss and follow the instructions. 

**Step 3:** Run the program, and don’t forget to provide the path to the downloaded directory (Codes of the contest) as a command line argument when running the program.



