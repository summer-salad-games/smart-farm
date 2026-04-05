class MathUtils:

    @staticmethod
    def map(value, min_value, max_value, target_min=0, target_max=100, flipped=False):
        if value < min_value:
            value = min_value
        elif value > max_value:
            value = max_value
        mapped_value = ((value - min_value) / (max_value - min_value)) * (target_max - target_min) + target_min
        return target_max - mapped_value if flipped else mapped_value