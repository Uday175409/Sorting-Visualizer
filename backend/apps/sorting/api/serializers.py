from rest_framework import serializers

class SortRequestSerializer(serializers.Serializer):
    ALGORITHM_CHOICES = [
        ('bubble', 'Bubble Sort'),
        ('selection', 'Selection Sort'),
        ('insertion', 'Insertion Sort'),
        ('merge', 'Merge Sort'),
        ('quick', 'Quick Sort'),
        ('heap', 'Heap Sort'),
    ]
    
    algorithm = serializers.ChoiceField(choices=ALGORITHM_CHOICES)
    array = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )
    speed = serializers.CharField(required=False, default="medium")

class SortResponseSerializer(serializers.Serializer):
    steps = serializers.ListField(child=serializers.DictField()) # Changed from child ListField to DictField
    sorted_array = serializers.ListField(child=serializers.IntegerField())
    metrics = serializers.DictField()
    complexity = serializers.DictField()
