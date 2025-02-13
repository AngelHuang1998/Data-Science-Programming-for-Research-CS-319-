"""Helper functions for printing out feedback to the student."""

from typing import List


def formatted_print(messages: List[str], section_title: str) -> None:
    """Helper function for print_feedback functions

    Prints out a list of messages as bullet points with whitespace above
    to improve readability. Section title describes the group of messages.

    Parameters:
        messages: The messages to print
        section_title: What to print above the messages to describe them
    """

    print(f"\n{section_title}")
    for msg in messages:
        print(f"  - {msg}")
