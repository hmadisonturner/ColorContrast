#!/usr/bin/env python3
"""
Color Contrast Calculator

A tool to calculate the contrast ratio between two colors according to WCAG guidelines.
Includes both a programmatic API and a command-line interface.
"""

import argparse
import sys
import re


def get_luminance(r, g, b):
    """
    Calculate the relative luminance of an RGB color.

    Args:
        r, g, b: RGB color values (0-255)

    Returns:
        The relative luminance value
    """
    # Normalize RGB values to range 0-1
    r = r / 255
    g = g / 255
    b = b / 255

    # Apply transformation
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

    # Calculate luminance using WCAG formula
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(rgb1, rgb2):
    """
    Calculate the contrast ratio between two RGB colors according to WCAG guidelines.

    Args:
        rgb1: Tuple of (r, g, b) values for the first color (0-255)
        rgb2: Tuple of (r, g, b) values for the second color (0-255)

    Returns:
        The contrast ratio as a float (1:1 to 21:1)
    """
    # Calculate luminance for both colors
    l1 = get_luminance(*rgb1)
    l2 = get_luminance(*rgb2)

    # Ensure l1 is the lighter color (higher luminance)
    if l1 < l2:
        l1, l2 = l2, l1

    # Calculate contrast ratio
    return (l1 + 0.05) / (l2 + 0.05)


def evaluate_wcag_compliance(contrast_ratio):
    """
    Evaluate WCAG compliance based on contrast ratio.

    Args:
        contrast_ratio: The calculated contrast ratio

    Returns:
        Dictionary with compliance information
    """
    return {
        "ratio": f"{contrast_ratio:.2f}:1",
        "AA_large_text": contrast_ratio >= 3.0,
        "AA_normal_text": contrast_ratio >= 4.5,
        "AAA_large_text": contrast_ratio >= 4.5,
        "AAA_normal_text": contrast_ratio >= 7.0
    }


def hex_to_rgb(hex_color):
    """
    Convert a hexadecimal color string to RGB.

    Args:
        hex_color: A color string in hex format (e.g., "#FFFFFF" or "FFFFFF")

    Returns:
        Tuple of (r, g, b) values (0-255)
    """
    # Remove # if present
    hex_color = hex_color.lstrip('#')

    # Check for shorthand hex (e.g., #FFF)
    if len(hex_color) == 3:
        hex_color = ''.join([c * 2 for c in hex_color])

    # Convert to RGB
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def parse_color(color_str):
    """
    Parse color string in various formats.

    Args:
        color_str: Color string in hex format or comma-separated RGB

    Returns:
        Tuple of (r, g, b) values (0-255)
    """
    # Check if it's a hex color
    if color_str.startswith('#') or re.match(r'^[0-9A-Fa-f]{6}$', color_str):
        return hex_to_rgb(color_str)

    # Check if it's RGB format
    if ',' in color_str:
        try:
            r, g, b = map(int, color_str.split(','))
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return (r, g, b)
        except (ValueError, TypeError):
            pass

    raise ValueError(
        f"Invalid color format: {color_str}. Use hex format (#RRGGBB) or comma-separated RGB values (r,g,b)")


def print_colorized(text, fg=None, bg=None, bold=False):
    """
    Print text with ANSI color codes.

    Args:
        text: Text to print
        fg: Foreground color (30-37)
        bg: Background color (40-47)
        bold: Whether to make text bold
    """
    codes = []
    if bold:
        codes.append('1')
    if fg is not None:
        codes.append(str(fg))
    if bg is not None:
        codes.append(str(bg))

    if codes:
        code_str = ';'.join(codes)
        print(f"\033[{code_str}m{text}\033[0m")
    else:
        print(text)


def main():
    """Main function for CLI interface."""
    parser = argparse.ArgumentParser(
        description='Calculate contrast ratio between two colors according to WCAG guidelines.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python contrast.py "#FFFFFF" "#000000"
  python contrast.py FFFFFF 000000
  python contrast.py 255,255,255 0,0,0
  python contrast.py --verbose "#FFFFFF" "#000000"
        """)

    parser.add_argument(
        'color1',
        help='First color in hex format (#RRGGBB) or RGB format (r,g,b)')
    parser.add_argument(
        'color2',
        help='Second color in hex format (#RRGGBB) or RGB format (r,g,b)')
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Show detailed compliance information')

    args = parser.parse_args()

    try:
        # Parse colors
        rgb1 = parse_color(args.color1)
        rgb2 = parse_color(args.color2)

        # Calculate contrast ratio
        ratio = calculate_contrast_ratio(rgb1, rgb2)
        compliance = evaluate_wcag_compliance(ratio)

        # Print results
        print(f"\nContrast Ratio: {compliance['ratio']}")

        if args.verbose:
            print("\nWCAG Compliance:")

            def result_icon(passed): return "✓" if passed else "✗"
            # 32=green, 31=red
            def result_color(passed): return 32 if passed else 31

            print_colorized(
                f"  AA  Large Text: {result_icon(compliance['AA_large_text'])}",
                fg=result_color(
                    compliance['AA_large_text']))
            print_colorized(
                f"  AA  Normal Text: {result_icon(compliance['AA_normal_text'])}",
                fg=result_color(
                    compliance['AA_normal_text']))
            print_colorized(
                f"  AAA Large Text: {result_icon(compliance['AAA_large_text'])}",
                fg=result_color(
                    compliance['AAA_large_text']))
            print_colorized(
                f"  AAA Normal Text: {result_icon(compliance['AAA_normal_text'])}",
                fg=result_color(
                    compliance['AAA_normal_text']))

            print("\nWCAG Guidelines:")
            print("  - AA  Large Text: minimum 3:1 contrast ratio")
            print("  - AA  Normal Text: minimum 4.5:1 contrast ratio")
            print("  - AAA Large Text: minimum 4.5:1 contrast ratio")
            print("  - AAA Normal Text: minimum 7:1 contrast ratio")

            print(
                "\nNote: 'Large Text' is defined as 18pt (24px) or 14pt (18.5px) bold and larger")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
