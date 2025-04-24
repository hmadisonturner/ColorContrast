Good color contrast is essential for web accessibility and effective design. Sufficient contrast ensures text is readable for all users, including those with visual impairments or those using devices in bright environments. The WCAG guidelines provide standards for minimum contrast ratios to ensure content is perceivable for everyone.

Use this project to check if your color combinations meet accessibility standards and to create designs that are both beautiful and inclusive.

## Web Version 

### Link

[Use the Color Contrast Calculator](https://hmadisonturner.github.io/ColorContrast/web/index.html)

### Features

1. Interactive Color Selection

   - Color pickers for both text and background colors
   - Manual hex code input options
   - Real-time color preview swatches


2. Live Visual Preview

   - Shows how both large text and normal text appear with your selected colors
   - Updates in real-time as you change colors


3. Contrast Analysis

   - Displays the calculated contrast ratio
   - Shows WCAG compliance status for:

     - AA Level (Large Text): 3:1 minimum
     - AA Level (Normal Text): 4.5:1 minimum
     - AAA Level (Large Text): 4.5:1 minimum
     - AAA Level (Normal Text): 7:1 minimum


4. Visual Pass/Fail Indicators

   - Green indicators for passing combinations
   - Red indicators for failing combinations


## Python CLI Version

### Installation

```bash
# Clone the repository
git clone https://github.com/hmadisonturner/ColorContrast.git
cd ColorContrast/cli
```

### Usage 

```bash
# Basic usage with hex colors (with # prefix)
python contrast.py "#FFFFFF" "#000000"

# Basic usage with hex colors (without # prefix)
python contrast.py FFFFFF 000000

# Using RGB values
python contrast.py 255,255,255 0,0,0

# Verbose output with detailed compliance information
python contrast.py --verbose "#FFFFFF" "#000000"

```

### Features

1. Flexible Input Formats

   - Accepts hex colors with or without # prefix (e.g., #FFFFFF or FFFFFF)
   - Supports comma-separated RGB values (e.g., 255,255,255)
   - Handles shorthand hex notation (e.g., #FFF expands to #FFFFFF)


1. Command-Line Arguments

   - Two positional arguments for the colors to compare
   - Optional -v/--verbose flag for detailed output


1. User-Friendly Output

   - Basic mode: Shows just the contrast ratio
   - Verbose mode: Displays WCAG compliance with color-coded pass/fail indicators
   - Includes clear examples in the help text


1. Error Handling

   - Validates all color inputs
   - Provides clear error messages for invalid formats
   - Shows help text if input is incorrect





