import subprocess
import os

REPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEX_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab4.tex")
PDF_FILE = os.path.join(REPORT_DIR, "Cooper_Morgan_Lab4.pdf")

# --- IMAGE PATHS (update these to point to your saved plot files) ---
FIGURE_1 = "figures/placeholder1.png"
FIGURE_2 = "figures/placeholder2.png"
FIGURE_3 = "figures/placeholder3.png"
FIGURE_4 = "figures/placeholder4.png"

tex_content = r"""
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{parskip}
\usepackage{float}

\titleformat{\section}{\large\bfseries}{}{0em}{}
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}

\title{Lab 4: Temporal Difference Learning}
\author{Morgan Cooper \\ MSDS 684 --- Reinforcement Learning}
\date{\today}

\begin{document}
\maketitle
\newpage


\section{Section 1: Project Overview}

% 400-500 words
% Problem/Question: What RL problem are you investigating?
% Core Concepts: What RL concepts from Sutton & Barto are you exploring?
% Theoretical Grounding: How does this connect to theory from the readings?
% Environment Description: State space, action space, reward structure, termination conditions
% Expected Behavior: What do you hypothesize will happen and why?

TODO: Write project overview here.


\newpage
\section{Section 2: Deliverables}

\subsection{GitHub Repository}
\begin{verbatim}
GitHub Repository: https://github.com/cooper-rm/temporal-difference-learning
\end{verbatim}

\subsection{Implementation Summary}

% 100-150 words
% What you implemented (algorithms, environments)
% Experimental setup (e.g., "1000 episodes, 30 random seeds, epsilon=0.1")
% Key hyperparameters chosen
% NOT detailed pseudocode or line-by-line methods

TODO: Write implementation summary here.


\subsection{Key Results \& Analysis}

% 400-600 words + 2-4 visualizations
% NO raw code listings in PDF
% NO console output dumps
% Each figure must have detailed interpretive caption
% Discussion must address:
%   - What do results show about algorithm behavior?
%   - How do they relate to theory from Sutton & Barto? (cite chapters/sections)
%   - What didn't work as expected? Why?
%   - How did hyperparameters affect performance?
%   - What does this teach you about the RL concept?

TODO: Write key results and analysis here.

% Uncomment and update figures as needed:
%\begin{figure}[H]
%\centering
%\includegraphics[width=0.85\textwidth]{""" + FIGURE_1 + r"""}
%\caption{TODO: Interpretive caption for Figure 1.}
%\label{fig:figure1}
%\end{figure}

%\begin{figure}[H]
%\centering
%\includegraphics[width=0.85\textwidth]{""" + FIGURE_2 + r"""}
%\caption{TODO: Interpretive caption for Figure 2.}
%\label{fig:figure2}
%\end{figure}

%\begin{figure}[H]
%\centering
%\includegraphics[width=0.85\textwidth]{""" + FIGURE_3 + r"""}
%\caption{TODO: Interpretive caption for Figure 3.}
%\label{fig:figure3}
%\end{figure}

%\begin{figure}[H]
%\centering
%\includegraphics[width=0.85\textwidth]{""" + FIGURE_4 + r"""}
%\caption{TODO: Interpretive caption for Figure 4.}
%\label{fig:figure4}
%\end{figure}


\section{Section 3: AI Use Reflection}

\subsection{Initial Interaction}

% 50-75 words
% What did you ask the AI to help you with?
% What was your initial prompt?
% What code/explanation did it provide?

TODO: Write initial interaction here.

\subsection{Iteration Cycle}

% 150-200 words --- MOST IMPORTANT
% Describe at least 2-3 concrete debugging cycles with:
%   - The error/problem you encountered
%   - Your follow-up prompt to AI
%   - AI's response
%   - Whether it worked or needed more iteration

TODO: Write iteration cycles here.

\subsection{Critical Evaluation}

% 50-75 words
% Did you catch any mistakes the AI made?
% Did you test alternative approaches?
% How did you verify the final solution was correct?

TODO: Write critical evaluation here.

\subsection{Learning Reflection}

% 50-75 words
% What did you learn about the RL algorithm through debugging?
% What did you learn about working with AI tools?
% What would you do differently next time?

TODO: Write learning reflection here.

\section{Section 4: Speaker Notes}

% 5-7 bullet points covering:
%   - Problem statement and motivation
%   - Method and key algorithmic choices
%   - Important design decision or challenge you faced
%   - Main result or finding
%   - Key insight or learning
%   - (Optional) Connection to future weeks or real-world applications

\begin{itemize}
  \item \textbf{Problem:} TODO
  \item \textbf{Method:} TODO
  \item \textbf{Design choice:} TODO
  \item \textbf{Key result:} TODO
  \item \textbf{Insight:} TODO
  \item \textbf{Challenge:} TODO
  \item \textbf{Connection:} TODO
\end{itemize}

\section{References}

\begin{enumerate}
  \item Sutton, R. S., \& Barto, A. G. (2018). \textit{Reinforcement learning: An introduction} (2nd ed.). MIT Press.
  \item Anthropic. (2025). Claude Code [Large language model CLI tool]. \texttt{https://claude.ai}
  \item OpenAI. (2025). ChatGPT [Large language model]. \texttt{https://chat.openai.com}
\end{enumerate}

\end{document}
"""

def main():

    # Write temporary .tex file
    with open(TEX_FILE, "w") as f:
        f.write(tex_content)

    # Compile to PDF (run twice to resolve cross-references)
    for pass_num in (1, 2):
        print(f"Compiling to PDF (pass {pass_num})...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", TEX_FILE],
            cwd=REPORT_DIR,
            capture_output=True,
            text=True,
        )

    if result.returncode == 0:
        print(f"PDF generated: {PDF_FILE}")
    else:
        print("pdflatex encountered issues:")
        print(result.stdout[-2000:] if len(result.stdout) > 2000 else result.stdout)

    # Clean up all LaTeX artifacts (keep only the PDF)
    for ext in [".tex", ".aux", ".log", ".out"]:
        artifact = os.path.join(REPORT_DIR, f"Cooper_Morgan_Lab4{ext}")
        if os.path.exists(artifact):
            os.remove(artifact)


if __name__ == "__main__":
    main()
