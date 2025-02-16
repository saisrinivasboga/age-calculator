from datetime import datetime

def calculate_age(birth_date):
    # Get current date and time
    current_datetime = datetime.now()
    
    # Convert input string to datetime object
    birth_datetime = datetime.strptime(birth_date, "%Y-%m-%d")
    
    # Calculate age difference
    age_timedelta = current_datetime - birth_datetime
    
    # Extract details
    years = age_timedelta.days // 365
    months = (age_timedelta.days % 365) // 30
    days = (age_timedelta.days % 365) % 30
    hours = age_timedelta.seconds // 3600
    minutes = (age_timedelta.seconds % 3600) // 60
    seconds = age_timedelta.seconds % 60

    # Display result
    print(f"\nYour exact age is:")
    print(f"{years} years, {months} months, {days} days")
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds old!")

# Get user input
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")
calculate_age(birth_date)
