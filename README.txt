# MASS: A Fast Product Kernel Density Analysis

## Overview
This QGIS plugin implements a fast product kernel density analysis method designed for efficient spatial analysis of large geospatial datasets.  
The plugin focuses on improving the computational performance of kernel density estimation while preserving accuracy, making it suitable for large-scale spatial experiments and research use.

## Functionality
- Perform kernel density analysis based on product kernels
- Support large datasets through optimized computation
- Generate density-related results for further analysis and visualization

## Input Data
- **Input format:** `.dat` file  
- The input `.dat` file contains experimental spatial data used for kernel density analysis.
- The user must **manually select** the input experimental data file when running the plugin.

## Output Data
- **Output format:** `.txt` file  
- The output `.txt` file stores the computed results of the kernel density analysis.
- The user must **manually specify** the destination and filename for the output `.txt` file.

## Usage Workflow
1. Open QGIS and load the plugin.
2. Launch the MASS kernel density analysis tool.
3. Manually select the input experimental data file (`.dat`).
4. Choose the location and name of the output result file (`.txt`).
5. Run the analysis and wait for the computation to finish.
6. Use the generated `.txt` file for further analysis or visualization.

## Notes
- This plugin is intended for research and experimental purposes.
- Ensure that the input `.dat` file follows the expected data format before running the analysis.
- Large datasets may require additional computation time depending on hardware resources.

## License
This plugin is released under the **GNU General Public License v2 or later (GPL-2.0-or-later)**.
