# Marginal Analysis — Market Garden (Case 1, Stage 1.2)

Determines the profit-maximizing bed allocation (tomatoes, carrots, mesclun) across 64 beds
for a price-taking market garden, using a Solver-based nonlinear optimization.

## Contents

- `spec.md` — the specification: inputs, calculation logic, validation tolerances, and the
  step-by-step reproduction procedure.
- `model.xlsx` — the workbook, built to the spec. Five sheets: Inputs, Labor, Cost,
  Optimization, Checks. Solver-optimal mix: Tomatoes 10 / Carrots 20 / Mesclun 30 beds,
  season profit ≈ $42,762.

## Reproducing the result

See the "Reproduction" section of `spec.md` for the full step-by-step procedure (Solver
setup, changing cells, constraints, and the checks to confirm on the Checks sheet).
