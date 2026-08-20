from statsmodels.stats.power import TTestIndPower

# Conservative standardized effect for the primary contrast: AI mental-state dialogue
# versus AI content-matched active control. The analysis will use baseline-adjusted outcomes.
raw_effect = 0.30
baseline_post_correlation = 0.60
adjusted_effect = raw_effect / (1 - baseline_post_correlation ** 2) ** 0.5

# Two primary planned contrasts use Holm control; calculate at the conservative first-test alpha.
alpha = 0.025
power = 0.95
attrition = 0.15
n_arms = 4

analysis = TTestIndPower()
n_per_arm_complete = analysis.solve_power(
    effect_size=adjusted_effect,
    alpha=alpha,
    power=power,
    ratio=1.0,
    alternative='two-sided',
)

n_per_arm_complete = int(n_per_arm_complete + 0.999999)
n_per_arm_recruited = int(n_per_arm_complete / (1 - attrition) + 0.999999)

print(f"Raw standardized effect: {raw_effect:.3f}")
print(f"Baseline-post correlation: {baseline_post_correlation:.2f}")
print(f"ANCOVA-adjusted standardized effect: {adjusted_effect:.3f}")
print(f"Conservative per-contrast alpha: {alpha:.3f}; target power: {power:.2f}")
print(f"Required completers per arm (two-arm primary contrast): {n_per_arm_complete}")
print(f"Required recruited participants per arm at {attrition:.0%} attrition: {n_per_arm_recruited}")
print(f"Four-arm target enrollment: {n_per_arm_recruited * n_arms}")
print("Note: a simulation-based power analysis for the final ordinal/IRT mixed model must retain or increase this target before registration.")
