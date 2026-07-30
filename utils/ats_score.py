def calculate_ats_score(match_score):
    """
    Convert the match percentage into an ATS score.
    """
    if match_score >= 80:
        return "Excellent", match_score
    elif match_score >= 60:
        return "Good", match_score
    elif match_score >= 40:
        return "Average", match_score
    else:
        return "Needs Improvement", match_score