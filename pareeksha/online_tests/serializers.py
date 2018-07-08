from rest_framework import serializers
from .models import Subject, Topic, OnlineTest, Problem, Option

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', )

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', )

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'statement', 'is_correct')
        extra_kwargs = {
            'is_correct': {'write_only': True},
        }

class ProblemSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)
    
    class Meta:
        model = Problem
        fields = ('id', 'statement', 'options')

class OnlineTestSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True, required=False)
    topic = TopicSerializer(many=False, required=False)
    creator = serializers.CharField(source='creator.email', read_only=True)
    
    class Meta:
        model = OnlineTest
        fields = ('id', 'title', 'description', 'created_at', 'problems', 'creator', 'topic', 
                    'starts_at', 'ends_at', 'duration_hours', 'duration_minutes', )

    def create(self, validated_data):
        problems_data = []
        if validated_data.get('problems', []):
            problems_data = validated_data.pop('problems')

        online_test = OnlineTest.objects.create(**validated_data)
            
        for problem_data in problems_data:
            options_data = []
            if problem_data.get('options'):
                options_data = problem_data.pop('options')
            
            problem = Problem.objects.create(test=online_test, **problem_data)
            for option_data in options_data:
                Option.objects.create(problem=problem, **option_data)
        
        return online_test

    def update(self, instance, validated_data):
        if self.partial:
            instance.title = validated_data.get('title', instance.title)
            instance.description = validated_data.get('description', instance.description)
            instance.starts_at = validated_data.get('starts_at', instance.starts_at)
            instance.ends_at = validated_data.get('ends_at', instance.ends_at)
            instance.duration_hours = validated_data.get('duration_hours', instance.duration_hours)
            instance.duration_minutes = validated_data.get('duration_minutes', instance.duration_minutes)
            if 'problems' in validated_data:
                instance.problems.all().delete()

        else:
            instance.title = validated_data.get('title')
            instance.description = validated_data.get('description')
            instance.starts_at = validated_data.get('starts_at')
            instance.ends_at = validated_data.get('ends_at')
            instance.duration_hours = validated_data.get('duration_hours')
            instance.duration_minutes = validated_data.get('duration_minutes')
            instance.problems.all().delete()
        
        problems_data = []
        if validated_data.get('problems'):
            problems_data = validated_data.pop('problems')
        
        instance.save()
            
        for problem_data in problems_data:
            options_data = []
            if problem_data.get('options'):
                options_data = problem_data.pop('options')
            
            problem = Problem.objects.create(test=instance, **problem_data)
            for option_data in options_data:
                Option.objects.create(problem=problem, **option_data)
        
        return instance
