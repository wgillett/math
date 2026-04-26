Write a Python script that does the following:
For each even number N from 5 to 1000, find all prime pairs (P, Q) that add up to N
Plot a graph (using matplotlib or your favorite python library):
X axis even numbers from 5 to 100
Y axis: for a given X value, place colored dots on the (P, Q) pairs for each N. Each (P, Q) pair should have a different color from other (P, Q) pairs. Example: 
3 + 13 = 16
5 + 11 = 16
You could color (3, 13) red and (5, 11) blue.

Generate colors dynamically using the golden angle method on a white background:
- Hue: (i × 137.508) % 360  — golden angle ensures successive hues never cluster
- Saturation: 0.75
- Lightness: 0.40  — dark enough to contrast with white (WCAG AA contrast ratio ~4–5:1)
- Convert with colorsys.hls_to_rgb (Python stdlib, no extra dependencies)
This produces as many distinct colors as needed with O(1) cost per color.