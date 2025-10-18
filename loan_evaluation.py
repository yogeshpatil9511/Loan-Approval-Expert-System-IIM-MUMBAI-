# --- Collateral Evaluation ---
def assign_collateral_rating(asset_info):
    """Assigns a 1-5 rating based on asset's liquidity, value stability, and legal clarity."""
    liquidity_score = {'high': 5, 'medium': 3, 'low': 1}
    stability_score = {'stable': 5, 'moderate': 3, 'volatile': 1}
    legal_score = {'clear': 5, 'minor_issues': 3, 'issues': 1}
    liquidity = asset_info.get('liquidity', 'low')
    stability = asset_info.get('stability', 'volatile')
    legal_clarity = asset_info.get('legal_clarity', 'issues')
    score = (liquidity_score[liquidity] * 0.5 +
             stability_score[stability] * 0.3 +
             legal_score[legal_clarity] * 0.2)
    return round(score)

def calculate_collateral_score(ratings, weights):
    """Calculate weighted average of collateral ratings."""
    total_score, total_weight = 0, 0
    for k, w in weights.items():
        if k in ratings:
            total_score += ratings[k] * w
            total_weight += w
    return total_score / total_weight if total_weight else 1

def calibrate_collateral(score):
    """Calibrate collateral score to 1-4 scale."""
    if score >= 4.5:
        return 4  # Excellent
    elif score >= 3.5:
        return 3  # Good
    elif score >= 2.5:
        return 2  # Medium
    else:
        return 1  # Poor

# --- Financial Evaluation ---
def calculate_financial_score(ratings, weights):
    """Calculate weighted average of financial factors."""
    total_score, total_weight = 0, 0
    for k, w in weights.items():
        if k in ratings:
            total_score += ratings[k] * w
            total_weight += w
    return total_score / total_weight if total_weight else 1

def calibrate_financial(score):
    """Calibrate financial score to 1-4 scale."""
    if score >= 4.5:
        return 4  # Excellent
    elif score >= 3.5:
        return 3  # Good
    elif score >= 2.5:
        return 2  # Medium
    else:
        return 1  # Bad

# --- Bank Profitability (Yield) ---
def assign_yield_rating(profitability_info):
    """Assigns a 1-3 rating based on loan profitability."""
    return profitability_info.get('yield_rating', 1)  # Default to 1 (Poor) if not provided