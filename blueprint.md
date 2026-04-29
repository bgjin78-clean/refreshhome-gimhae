# Lotto Number Generator

## Overview

A polished web application to generate multiple sets of lucky lottery numbers with a modern, interactive UI.

## Features

*   **5 Sets of Numbers**: Generates 5 independent sets of 6 unique random numbers between 1 and 45.
*   **Lotto Ball Styling**: Numbers are displayed in colored balls based on their value ranges:
    *   1-10: Yellow (#fbc02d)
    *   11-20: Blue (#1976d2)
    *   21-30: Red (#e53935)
    *   31-40: Gray (#757575)
    *   41-45: Green (#43a047)
*   **Interactive Animations**: Balls pop in with a smooth animation when generated.
*   **Mobile Optimized**: Responsive design that scales and stacks sets beautifully on all screen sizes.
*   **Modern Aesthetics**: Deep shadows, vibrant gradients, and a subtle background texture.

## Implementation Plan

1.  **Update `style.css`**:
    *   Define color classes for the Lotto ball ranges.
    *   Add `@keyframes` for the "pop-in" animation.
    *   Implement container queries or improved media queries for row management.
    *   Add a subtle noise texture and deep shadows as per GEMINI.md guidelines.
2.  **Update `main.js`**:
    *   Refactor the generation logic to produce 5 sets.
    *   Assign appropriate color classes based on the number value.
    *   Implement a staggered animation delay for a better user experience.
3.  **Update `index.html`**:
    *   Ensure the structure supports multiple rows of balls.
