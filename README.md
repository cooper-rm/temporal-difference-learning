# Temporal Difference Learning

MSDS 684 - Reinforcement Learning | Lab 4 | Morgan Cooper

## Overview

This project implements and compares SARSA (on-policy) and Q-learning (off-policy) on Gymnasium's CliffWalking-v1 environment. Both agents use the same structure — same Q-table, same epsilon-greedy exploration — with only one line different in the TD update. That single difference leads to completely different learned paths.

## Results

- **SARSA**: Learns the safe path across the top of the grid (-28.0 avg training reward, 17-step greedy policy)
- **Q-learning**: Learns the optimal cliff-edge path (-51.6 avg training reward, 13-step greedy policy)
- **Epsilon decay**: Exponential decay improved Q-learning from -50.5 to -16.8, eventually beating SARSA

## Environment

**CliffWalking-v1**: A 4x12 gridworld (48 states, 4 actions). Agent starts bottom-left, goal is bottom-right. The bottom edge between start and goal is a cliff — stepping on it gives -100 reward and resets to start. Every other step gives -1.

## Files

- `Lab4_TD_Learning.ipynb` — Main notebook with all implementations and visualizations
- `generate_report.py` — Generates the LaTeX report PDF
- `figures/` — Saved plots for the report
- `Cooper_Morgan_Lab4.pdf` — Final report

## Usage

```bash
# Run the notebook first, then generate the report
python generate_report.py
```
