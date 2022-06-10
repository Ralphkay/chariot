# # Signals
# import datetime
#
# from django.db.models import F
# from django.db.models.signals import post_save, post_delete, pre_save
# from django.dispatch import receiver
#
# from membership.models import Member, TrackDailyActivities, Levy
#
#
# @receiver(post_save, sender=Member)
# def member_created(sender, instance, created, *args, **kwargs):
#     current_date_created_member = datetime.datetime.date(instance.created_on)
#     # Get last record of member and its date
#     try:
#         last_record = Member.objects.latest('created_on')
#         all_members = Member.objects.count()
#         date_of_last_record_created = datetime.datetime.date(last_record.created_on)
#         # if date_of_last_record_created is less than today then is the first record
#         if created:
#             if last_record is None:
#                 if date_of_last_record_created < datetime.datetime.today().date():
#                     print("first condition runs: creating new activity")
#                     TrackDailyActivities.objects.create(members_registered_today=1)
#
#             if last_record and all_members > 1:
#                 if date_of_last_record_created < datetime.datetime.today().date():
#                     print("first condition runs: creating new activity")
#                     TrackDailyActivities.objects.create(members_registered_today=1)
#
#                 elif date_of_last_record_created == datetime.datetime.today().date():
#                     print("second condition is running")
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                         update(members_registered_today=F('members_registered_today') + 1)
#                 else:
#                     if current_date_created_member == date_of_last_record_created:
#                         print("updating daily activity", current_date_created_member, date_of_last_record_created)
#                         TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                             update(members_registered_today=F('members_registered_today') + 1)
#             else:
#                 TrackDailyActivities.objects.create(members_registered_today=1)
#     except:
#         last_record = None
#
# @receiver(post_delete, sender=Member)
# def member_deleted(sender, instance, **kwargs):
#     current_date_created_member = datetime.datetime.date(instance.created_on)
#     # Get last record of member and its date
#     try:
#         last_record = Member.objects.latest('created_on')
#         all_members = Member.objects.count()
#         date_of_last_record_created = datetime.datetime.date(last_record.created_on)
#
#         if instance:
#             if last_record and all_members > 1:
#                 if date_of_last_record_created < datetime.datetime.today().date():
#                     print("first condition runs: creating new activity")
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                         update(members_registered_today=F('members_registered_today') - 1)
#
#                 elif date_of_last_record_created == datetime.datetime.today().date():
#                     print("second condition is running")
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                         update(members_registered_today=F('members_registered_today') - 1)
#                 else:
#                     if current_date_created_member == date_of_last_record_created:
#                         print("updating daily activity", current_date_created_member, date_of_last_record_created)
#                         TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                             update(members_registered_today=F('members_registered_today') - 1)
#             else:
#                 TrackDailyActivities.objects.filter(created_on__date=current_date_created_member). \
#                     update(members_registered_today=F('members_registered_today') - 1)
#
#     except:
#         last_record =None
# @receiver(pre_save, sender=Levy)
# def before_levy_created(sender, instance, **kwargs):
#     try:
#         previous_month_levy_paid = Levy.objects.get(id=instance.id)
#         current_date_created_levy = datetime.datetime.date(instance.created_on)
#         # Get last record of member and its date
#         last_record = Levy.objects.latest('created_on')
#         all_levies = Levy.objects.count()
#         date_of_last_record_created = datetime.datetime.date(last_record.created_on)
#
#         if previous_month_levy_paid.month_levy_paid < instance.month_levy_paid:
#             TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                 update(total_levies_collected_today=F('total_levies_collected_today') + instance.month_levy_paid)
#
#         if previous_month_levy_paid.month_levy_paid > instance.month_levy_paid:
#             TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                 update(total_levies_collected_today=F('total_levies_collected_today') - instance.month_levy_paid)
#
#         if previous_month_levy_paid.month_levy_paid == instance.month_levy_paid:
#             TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                 update(total_levies_collected_today=F('total_levies_collected_today') + 0 )
#     except:
#         previous_month_levy_paid = None
#
# @receiver(post_save, sender=Levy)
# def levy_created(sender, instance, created, *args, **kwargs):
#     current_date_created_levy = datetime.datetime.date(instance.created_on)
#     # Get last record of member and its date
#     last_record = Levy.objects.latest('created_on')
#     all_levies = Levy.objects.count()
#     date_of_last_record_created = datetime.datetime.date(last_record.created_on)
#     # if date_of_last_record_created is less than today then is the first record
#     if created:
#         if last_record and all_levies > 1:
#             if date_of_last_record_created < datetime.datetime.today().date():
#                 print("first condition runs: creating new activity")
#                 TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                     update(total_levies_collected_today=F('total_levies_collected_today') + instance.month_levy_paid)
#             elif date_of_last_record_created == datetime.datetime.today().date():
#                 print("second condition is running")
#                 TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                     update(total_levies_collected_today=F('total_levies_collected_today') + instance.month_levy_paid)
#             else:
#                 if current_date_created_levy == date_of_last_record_created:
#                     print("updating daily activity", current_date_created_levy, date_of_last_record_created)
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                         update(
#                         total_levies_collected_today=F('total_levies_collected_today') + instance.month_levy_paid)
#         else:
#             TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                 update(total_levies_collected_today=F('total_levies_collected_today') + instance.month_levy_paid)
#
#
# @receiver(post_delete, sender=Levy)
# def levy_deleted(sender, instance, **kwargs):
#     current_date_created_levy = datetime.datetime.date(instance.created_on)
#     # Get last record of member and its date
#     try:
#         last_record = Levy.objects.latest('created_on')
#
#         all_levies = Levy.objects.count()
#         date_of_last_record_created = datetime.datetime.date(last_record.created_on)
#         # if date_of_last_record_created is less than today then is the first record
#         if instance:
#             if last_record and all_levies > 1:
#                 if date_of_last_record_created < datetime.datetime.today().date():
#                     print("first condition runs: creating new activity")
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                         update(total_levies_collected_today=F('total_levies_collected_today') - instance.month_levy_paid)
#                 elif date_of_last_record_created == datetime.datetime.today().date():
#                     print("second condition is running")
#                     TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                         update(total_levies_collected_today=F('total_levies_collected_today') - instance.month_levy_paid)
#                 else:
#                     if current_date_created_levy == date_of_last_record_created:
#                         print("updating daily activity", current_date_created_levy, date_of_last_record_created)
#                         TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                             update(
#                             total_levies_collected_today=F('total_levies_collected_today') - instance.month_levy_paid)
#             else:
#                 TrackDailyActivities.objects.filter(created_on__date=current_date_created_levy). \
#                     update(total_levies_collected_today=F('total_levies_collected_today') - instance.month_levy_paid)
#     except:
#         last_record = None