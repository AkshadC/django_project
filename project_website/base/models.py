from django.contrib.auth.models import Group, User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

MODEL_NAMES = ['Fujitsu_Connections', "Tdm_CrossConnects_Ericsson", "VLAN_CrossConnects_Ericsson",  "Processed_TAS_Auth_Sheet",
               "Associated_Traffic_By_Network_Element", "Pipe_Data", "Services", "RAD_Time_Slots", "Rad_Imported_Services", "Fujitsu_Links", 
               "Fujitsu_Pipes"]
class Services(models.Model):
    
    sv_id = models.CharField(("SV ID"), max_length = 100, primary_key = True)
    service_name = models.CharField(("Service Name"), max_length = 100)
    service_profile = models.CharField(("Service Profile"), max_length = 100)
    service_connections = models.CharField(("Service Connections"), max_length = 100)    
    start_ne = models.CharField(("Start NE"), max_length = 100)
    end_ne = models.CharField(("End NE"), max_length = 100)
    
    class Meta:
        verbose_name = _("Services")
        verbose_name_plural = _("Services")
    
    def __str__(self):
        return self.service_name


class Fujitsu_Connections(models.Model):
    
    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    connectionName = models.CharField(("Connection Name"), max_length = 150) 
    state = models.CharField(("Service State"), max_length = 50)
    rate = models.CharField(("Service Bandwidth Rate"), max_length = 50)
    layer = models.CharField(("Connection Layer"), max_length = 50)
    direction = models.CharField(("Service Direction"), max_length = 50)
    path_group_info_list = models.CharField(("Path Group Information List"), max_length = 250)
    
    class Meta:
        
        db_table = 'Fujitsu_Connections'
        verbose_name = "Fujitsu_Connections"
        verbose_name_plural = "Fujitsu_Connections"
        
    def __str__(self):
        return self.connectionName
    
class Tdm_CrossConnects_Ericsson(models.Model):
    
    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)

    service_auth_number = models.CharField(("Auth Number"), max_length = 50)
    service_auth_desc = models.CharField(("Auth Description"), max_length = 100)
    interface_1 = models.CharField(("Interface 1"), max_length = 50)
    interface_2 = models.CharField(("Interface 2"), max_length = 50)
    
    class Meta:
        verbose_name = _("Tdm_CrossConnects_Ericsson")
        verbose_name_plural = _("Tdm_CrossConnects_Ericsson")
    
    def __str__(self):
        return self.service_auth_number
    
class VLAN_CrossConnects_Ericsson(models.Model):

    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    service_auth_number = models.CharField(("Service Auth Number"), max_length = 50)
    service_auth_desc = models.CharField(("Auth Description"), max_length = 100)
    egress_ports = models.CharField(("Egress ports"), max_length = 100)
    
    class Meta:
        verbose_name = _("VLAN_CrossConnects_Ericsson")
        verbose_name_plural = _("VLAN_CrossConnects_Ericsson")
    
    def __str__(self):
        return self.service_auth_number
    
class Processed_TAS_Auth_Sheet(models.Model):

    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    channel_auth_number = models.CharField(("Channel Auth Number"), max_length = 100)
    primary_device_list = models.CharField(("Primary Device List"), max_length = 200)
    secondary_device_list = models.CharField(("Secondary Device List"), max_length = 200)
    inferred_path = models.CharField(("Inferred Path for the Service"), max_length = 100)
    
    class Meta:
        verbose_name = _("Processed_TAS_Auth_Sheet")
        verbose_name_plural = _("Processed_TAS_Auth_Sheet")
    
    def __str__(self):
        return self.channel_auth_number
    
class Associated_Traffic_By_Network_Element(models.Model):
    
    profile = models.CharField(("Service Profile"), max_length = 100)
    exceptions = models.CharField(("Exceptions"), max_length = 100)
    start_aid = models.CharField(("Start AID"), max_length = 100)
    end_aid = models.CharField(("END AID"), max_length = 100)
    svc_id = models.CharField(("Service ID"), max_length = 100)
    svc_desc = models.CharField(("Service Description"), max_length = 100)
    svc_name = models.CharField(("Service Name"), max_length = 100)
    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    start_ne = models.CharField(("Start NE"), max_length = 100)
    end_ne = models.CharField(("End NE"), max_length = 100)
    parent_ne_id = models.CharField(("Parent NE ID"), max_length = 100)
    
    class Meta:
        verbose_name = _("Associated_Traffic_By_Network_Element")
        verbose_name_plural = _("Associated_Traffic_By_Network_Element")
    
    def __str__(self):
        return self.svc_id
    
class Pipe_Data(models.Model):
    
    sv_id = models.CharField(("SV ID"), primary_key = True, max_length = 100)
    pipe_id = models.CharField(("Pipe ID"), max_length = 100)
    pipe_name = models.CharField(("Pipe Name"), max_length = 100)
    start_ne = models.CharField(("Start NE"), max_length = 100)
    end_ne = models.CharField(("End NE"), max_length = 100)
    connections = models.CharField(("Connections"), max_length = 100)
    profile = models.CharField(("Profile"), max_length = 100)
    
    class Meta:
        verbose_name = _("Pipe_Data")
        verbose_name_plural = _("Pipe_Data")
    
    def __str__(self):
        return self.pipe_id
      
class RAD_Time_Slots(models.Model):
    
    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    service_auth_number = models.CharField(("Service Auth Number"), max_length = 100)
    path_name = models.CharField(("Path Name"), max_length = 100)
    source_name = models.CharField(("Source Name"), max_length = 100)
    source_slot = models.CharField(("Source Slot"), max_length = 100)
    source_port = models.CharField(("Source Port"), max_length = 100)
    source_card_type = models.CharField(("Source Card Type"), max_length = 100)
    
    destination_name = models.CharField(("Destination Name"), max_length = 100)
    destination_slot = models.CharField(("Destination Slot"), max_length = 100)
    destination_port = models.CharField(("Destination Port"), max_length = 100)
    destination_card_type = models.CharField(("Destination Card Type"), max_length = 100)
    network_link = models.CharField(("Network Link"), max_length = 100)
    time_slots = models.CharField(("Timeslots"), max_length = 100)
    
    class Meta:
        verbose_name = _("RAD_Time_Slots")
        verbose_name_plural = _("RAD_Time_Slots")
    
    def __str__(self):
        return self.service_auth_number
    
class Rad_Imported_Services(models.Model):

    sv_id = models.ForeignKey(Services, to_field = 'sv_id', on_delete = models.DO_NOTHING)
    channel_auth_number = models.CharField(("Channel auth number"), max_length = 100)
    service_name = models.CharField(("Channel Auth Name"), max_length = 100)
    end_point_1_telenium = models.CharField((""), max_length = 100)
    end_point_2_telenium = models.CharField((""), max_length = 100)
    start_point = models.CharField(("Start device id"), max_length = 100)
    end_point = models.CharField(("End device id "), max_length = 100)
    
    class Meta:
        verbose_name = _("Rad_Imported_Services")
        verbose_name_plural = _("Rad_Imported_Services")
    
    def __str__(self):
        return self.channel_auth_number
    
class Fujitsu_Links(models.Model):
    
    rateA = models.CharField(("Rate A"), max_length = 100)
    rateZ = models.CharField(("Rate Z"), max_length = 100)
    link_name = models.CharField(("Link Name"), max_length = 100)
    ne_id_A = models.CharField(("NE ID A"), max_length = 100)
    ne_id_Z = models.CharField(("NE ID Z"), max_length = 100)
    link_rate = models.CharField(("Link Rate"), max_length = 100)
    
    class Meta:
        verbose_name = _("Fujitsu_Links")
        verbose_name_plural = _("Fujitsu_Links")
    
    def __str__(self):
        return self.link_name
    
class Fujitsu_Pipes(models.Model):

    pipe_name = models.CharField(("Pipe Name"), max_length = 100)
    pipe_starting_ne = models.CharField(("Pipe Starting NE"), max_length = 100)
    pipe_starting_aid = models.CharField(("Pipe Starting AID"), max_length = 100)
    pipe_ending_ne = models.CharField(("Pipe Ending NE"), max_length = 100)
    pip_ending_aid = models.CharField(("Pipe Ending AID"), max_length = 100)
    
    class Meta:
        verbose_name = _("Fujitsu_Pipes")
        verbose_name_plural = _("Fujitsu_Pipes")
    
    def __str__(self):
        return self.pipe_name
    
class BaseRevisionHistoryTable(models.Model):
    column_name = models.CharField(max_length = 100)
    old_value = models.TextField()
    new_value = models.TextField()
    changed_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    change_date = models.DateTimeField(default = timezone.now)
    class Meta:
        abstract = True
    
    def __str__(self):
        return f"Column {self.column_name} changed from {self.old_value} to {self.new_value}"

def create_revision_history_tables(table_name):
    return type(
        f"{table_name}RevHistory",
        (BaseRevisionHistoryTable,),
        {
            'table': models.ForeignKey(
                f"base.{table_name}", on_delete=models.DO_NOTHING
            ),
            '__module__': __name__,  # Ensure the module is set correctly
            'Meta': type('Meta', (), {
                'verbose_name': _(f"{table_name} Revision History"),
                'verbose_name_plural': _(f"{table_name} Revision Histories"),
            })
        }
    )
    
globals().update({f"{name}RevHistory": create_revision_history_tables(name) for name in MODEL_NAMES})