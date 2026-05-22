def map_it_act(section):
    """
    Map a given section to the IT Act.

    Args:
        section (str): Section of the IT Act.

    Returns:
        str: Description of the section.
    """
    it_act_mapping = {
        "66C": "Identity theft",
        "66D": "Cheating by personation",
        "67": "Publishing obscene material",
        "67A": "Publishing sexually explicit material"
    }
    return it_act_mapping.get(section, "Unknown section")