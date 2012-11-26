def get_threshold(datapoints, percentile=97, lower=None, upper=None):
    """Calculate a percentile based threshold."""
    sorted_points = sorted(datapoints)
    if percentile == 100:
        return sorted_points[-1]
    perc_value = sorted_points[percentile*len(datapoints)/100]
    if perc_value < lower:
        return lower
    elif perc_value > upper:
        return upper
    return perc_value
