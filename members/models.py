import datetime
from django.db import models

SECTIONS = [
    ("External Bodies", "External Bodies"), 
    ("Group", "Group"),
    ("Joey", "Joey"),
    ("Left", "Left"),
    ("Monday Cub", "Monday Cub"),
    ("Rover", "Rover"),
    ("Scout", "Scout"),
    ("Scouts Qld", "Scouts Qld"),
    ("Venturer", "Venturer"),
    ("Wednesday Cub", "Wednesday Cub"),
    ]

EMAIL_TYPES = [
    ("HTML", "HTML"), 
    ("Text", "Text"),
    ]

MEMBER_TYPES = [
    ("Adult Member", "Adult Member"),
    ("Associate Leader", "Associate Leader"),
    ("External Body", "External Body"),
    ("Full Youth Member", "Full Youth Member"),
    ("Non Member", "Non Member"),
    ("Probationary Leader", "Probationary Leader"),
    ("Second or Subsequent Child", "Second or Subsequent Child"),
    ("Trainee Leader", "Trainee Leader"),
    ("Woodbeaded Leader", "Woodbeaded Leader"),
    ]

HELP_TEXT = {
    "main_email_address":"Up to four emails can be added, separated by a semi-colon and no spaces. This is the only field that the system uses to send out emails.",
}

# Create your models here.
class Member(models.Model):
    address_1 = models.CharField(max_length=50, null=True, blank=True, verbose_name="Address 1")
    address_2 = models.CharField(max_length=50, null=True, blank=True, verbose_name="Address 2")
    adult_investiture = models.DateField(null=True, blank=True, verbose_name="Adult Investiture")
    medical_alert = models.BooleanField(default=False, null=True, blank=True, verbose_name="Medical Alert")
    carer_alert = models.BooleanField(default=False, null=True, blank=True, verbose_name="Carer Alert")
    financial_alert = models.BooleanField(default=False, null=True, blank=True, verbose_name="Financial Alert")
    general_alert = models.BooleanField(default=False, null=True, blank=True, verbose_name="General Alert")
    alert_notes = models.CharField(max_length=50, null=True, blank=True, verbose_name="Alert notes")
    allergies = models.CharField(max_length=100, null=True, blank=True, verbose_name="Allergies")
    ambulance_fund = models.CharField(max_length=30, null=True, blank=True, verbose_name="Ambulance Fund")
    app_form_issued = models.DateField(null=True, blank=True, verbose_name="App Form Issued")
    app_form_returned = models.DateField(null=True, blank=True, verbose_name="App Form Returned")
    app_sent_to_branch = models.DateField(null=True, blank=True, verbose_name="App Sent to Branch")
    appointment_review = models.DateField(null=True, blank=True, verbose_name="Appointment Review")
    blue_card_wwcc_first_issued = models.DateField(null=True, blank=True, verbose_name="Blue Card/WWCC First Issued")
    blue_card_wwcc_next_expires = models.DateField(null=True, blank=True, verbose_name="Blue Card/WWCC Next Expires")
    blue_card_wwcc_number = models.CharField(max_length=30, null=True, blank=True, verbose_name="Blue Card/WWCC Number")
    carer_1_blue_card_no = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Blue Card #")
    carer_1_blue_card_expiry = models.DateField(null=True, blank=True, verbose_name="Carer 1 Blue card expiry")
    carer_1_email = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Carer 1 Email")
    carer_1_employer = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Employer")
    carer_1_fax = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Fax")
    carer_1_help_offer = models.CharField(max_length=50, null=True, blank=True, verbose_name="Carer 1 Help offer")
    carer_1_interests = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Interests")
    carer_1_mobile = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Mobile")
    carer_1_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Name")
    carer_1_occupation = models.CharField(max_length=50, null=True, blank=True, verbose_name="Carer 1 Occupation")
    carer_1_previous_scouting = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Previous Scouting")
    carer_1_relationship = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Relationship")
    carer_1_skills = models.CharField(max_length=100, null=True, blank=True, verbose_name="Carer 1 Skills")
    carer_1_work_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 1 Work Phone")
    carer_2_blue_card_no = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Blue Card #")
    carer_2_blue_card_exp = models.DateField(null=True, blank=True, verbose_name="Carer 2 Blue Card Exp")
    carer_2_email = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Carer 2 Email")
    carer_2_employer = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Employer")
    carer_2_fax = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Fax")
    carer_2_help_offer = models.CharField(max_length=50, null=True, blank=True, verbose_name="Carer 2 Help offer")
    carer_2_interests = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Interests")
    carer_2_mobile = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Mobile")
    carer_2_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Name")
    carer_2_occupation = models.CharField(max_length=50, null=True, blank=True, verbose_name="Carer 2 Occupation")
    carer_2_previous_scouting = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Previous Scouting")
    carer_2_relationship = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Relationship")
    carer_2_skills = models.CharField(max_length=100, null=True, blank=True, verbose_name="Carer 2 Skills")
    carer_2_work_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Carer 2 Work Phone")
    change_type = models.CharField(max_length=30, null=True, blank=True, verbose_name="Change Type")
    contact_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Contact Phone")
    contact_phone1 = models.CharField(max_length=30, null=True, blank=True, verbose_name="Contact Phone.1")
    cpr_date = models.DateField(null=True, blank=True, verbose_name="CPR Date")
    cub_investiture = models.DateField(max_length=30, null=True, blank=True, verbose_name="Cub Investiture")
    date_left_scouting = models.DateField(null=True, blank=True, verbose_name="Date Left Scouting")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    dietary_preferences = models.CharField(max_length=30, null=True, blank=True, verbose_name="Dietary Preferences")
    disabilities = models.CharField(max_length=30, null=True, blank=True, verbose_name="Disabilities")
    doctors_phone = models.CharField(max_length=100, null=True, blank=True, verbose_name="Doctor's Phone")
    email_type = models.CharField(choices=EMAIL_TYPES, max_length=30, null=True, blank=True, verbose_name="Email Type")
    emergency_contact = models.CharField(max_length=30, null=True, blank=True, verbose_name="Emergency Contact")
    employer_school = models.CharField(max_length=30, null=True, blank=True, verbose_name="Employer/School")
    expiry_date = models.CharField(max_length=30, null=True, blank=True, verbose_name="Expiry Date")
    family_doctor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Family Doctor")
    family_notes = models.CharField(max_length=100, null=True, blank=True, verbose_name="Family notes")
    first_aid_cert = models.DateField(null=True, blank=True, verbose_name="First Aid Cert")
    first_invested = models.DateField(null=True, blank=True, verbose_name="First Invested")
    first_names = models.CharField(max_length=30, null=True, blank=True, verbose_name="First Names")
    gender = models.CharField(max_length=30, null=True, blank=True, verbose_name="Gender")
    heard_about_scouts = models.CharField(max_length=30, null=True, blank=True, verbose_name="Heard about Scouts")
    home_fax = models.CharField(max_length=30, null=True, blank=True, verbose_name="Home Fax")
    home_language = models.CharField(max_length=30, null=True, blank=True, verbose_name="Home Language")
    home_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Home Phone")
    image_file = models.CharField(max_length=30, null=True, blank=True, verbose_name="Image File")
    interests = models.CharField(max_length=30, null=True, blank=True, verbose_name="Interests")
    joey_investiture = models.DateField(max_length=30, null=True, blank=True, verbose_name="Joey Investiture")
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Last Name")
    last_review_date = models.DateField(null=True, blank=True, verbose_name="Last Review Date")
    last_tetanus_date = models.CharField(max_length=30, null=True, blank=True, verbose_name="Last Tetanus Date")
    main_email_address = models.EmailField(max_length=254, null=True, blank=True, verbose_name="Main Email Address", help_text=HELP_TEXT['main_email_address'])
    medical_action_plan = models.TextField(max_length=200, null=True, blank=True, verbose_name="Medical Action Plan")
    medical_conditions = models.TextField(max_length=200, null=True, blank=True, verbose_name="Medical conditions")
    medical_fund = models.CharField(max_length=30, null=True, blank=True, verbose_name="Medical Fund")
    medicare_number = models.CharField(max_length=30, null=True, blank=True, verbose_name="Medicare Number")
    medications = models.TextField(max_length=100, null=True, blank=True, verbose_name="Medications")
    member_type = models.CharField(choices=MEMBER_TYPES, max_length=30, null=True, blank=True, verbose_name="Member Type")
    membership_number = models.CharField(max_length=30, null=True, blank=True, verbose_name="Membership Number")
    mobile = models.CharField(max_length=50, null=True, blank=True, verbose_name="Mobile")
    nationality = models.CharField(max_length=30, null=True, blank=True, verbose_name="Nationality")
    occupation = models.CharField(max_length=30, null=True, blank=True, verbose_name="Occupation")
    place_of_birth = models.CharField(max_length=30, null=True, blank=True, verbose_name="Place of Birth")
    position_on_card = models.CharField(max_length=30, null=True, blank=True, verbose_name="Position on card")
    post_address_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Post Address 1")
    post_address_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="Post Address 2")
    postal_postcode = models.CharField(max_length=30, null=True, blank=True, verbose_name="Postal Postcode")
    postal_state = models.CharField(max_length=30, null=True, blank=True, verbose_name="Postal State")
    postal_suburb = models.CharField(max_length=30, null=True, blank=True, verbose_name="Postal Suburb")
    postcode = models.CharField(max_length=30, null=True, blank=True, verbose_name="Postcode")
    pref_strength = models.CharField(max_length=30, null=True, blank=True, verbose_name="Pref. Strength")
    preferred_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Preferred Name")
    qld_branch_family_code = models.CharField(max_length=30, null=True, blank=True, verbose_name="QLD Branch Family Code")
    quick_initials = models.CharField(max_length=30, null=True, blank=True, verbose_name="Quick Initials")
    rank = models.CharField(max_length=30, null=True, blank=True, verbose_name="Rank")
    record_created = models.DateField(null=True, blank=True, verbose_name="Record Created")
    relationship_to_member = models.CharField(max_length=30, null=True, blank=True, verbose_name="Relationship to member")
    religion = models.CharField(max_length=30, null=True, blank=True, verbose_name="Religion")
    residential_situation = models.CharField(max_length=30, null=True, blank=True, verbose_name="Residential Situation")
    rover_investiture = models.DateField(null=True, blank=True, verbose_name="Rover Investiture")
    salutation = models.CharField(max_length=30, null=True, blank=True, verbose_name="Salutation")
    scout_investiture = models.DateField(null=True, blank=True, verbose_name="Scout Investiture")
    scout_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Scout Name")
    section = models.CharField(choices=SECTIONS, max_length=30, null=True, blank=True, verbose_name="Section")
    sighted_blue_card = models.DateField(null=True, blank=True, verbose_name="Sighted Blue Card")
    six_patrol_group = models.CharField(max_length=50, null=True, blank=True, verbose_name="Six/Patrol/Group")
    social_media = models.CharField(max_length=30, null=True, blank=True, verbose_name="Social Media")
    source = models.CharField(max_length=30, null=True, blank=True, verbose_name="Source")
    state = models.CharField(max_length=30, null=True, blank=True, verbose_name="State")
    suburb = models.CharField(max_length=30, null=True, blank=True, verbose_name="Suburb")
    venturer_investiture = models.DateField(null=True, blank=True, verbose_name="Venturer Investiture")
    waiting_list_comment = models.CharField(max_length=30, null=True, blank=True, verbose_name="Waiting list comment")
    waiting_list_date = models.DateField(null=True, blank=True, verbose_name="Waiting List Date")
    where_to = models.CharField(max_length=30, null=True, blank=True, verbose_name="Where to?")
    work_fax = models.CharField(max_length=30, null=True, blank=True, verbose_name="Work Fax")
    work_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Work Phone")
    yh_appointment = models.DateField(null=True, blank=True, verbose_name="YH Appointment")  
    def __str__(self):
        return (self.first_names if self.first_names is not None else "{No first names}") + " " + (self.last_name if self.last_name is not None else "{No lastr name}")
