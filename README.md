## Web Version 

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


## Python CLI Version:

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


### Usage Examples:

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



