import random

def schedule_classes(subjects, classrooms, time_slots):
    # Create a shuffled list of time slots
    shuffled_time_slots = random.sample(range(time_slots), time_slots)

    # Assign time slots to subjects
    class_schedule = {}
    for i, subject in enumerate(subjects):
        class_schedule[subject] = shuffled_time_slots[i % time_slots]

    return class_schedule

def check_conflicts(class_schedule):
    # Check for conflicts using the Pigeonhole Principle
    pigeonhole = set()
    
    for subject, time_slot in class_schedule.items():
        if time_slot in pigeonhole:
            # Conflict detected
            return True
        pigeonhole.add(time_slot)

    # No conflicts
    return False

# Example Usage
subjects = ['Math', 'English', 'Science', 'History']
classrooms = int(input("Enter the number of classrooms: "))
print("The number of classrooms are: ", classrooms)

time_slots = int(input("Enter the number of time slots: "))
print("The time slots are: ", time_slots)

# Schedule classes
class_schedule = schedule_classes(subjects, classrooms, time_slots)

# Check for conflicts
conflict_exists = check_conflicts(class_schedule)

# Output
print("Class Schedule:")
for subject, time_slot in class_schedule.items():
    print(f"{subject}: Time Slot {time_slot + 1}")

if conflict_exists:
    print("\nConflict Detected: Two classes with the same subject are scheduled simultaneously.")
else:
    print("\nNo Conflict: All classes are scheduled without overlap.")
