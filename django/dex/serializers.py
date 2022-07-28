from rest_framework import serializers
#from popolo.models import Person, Organization, Membership, Post

from cities.models import City
#from dex.models.models_base import Org, BasePerson, Events
from dex.models.dx_cities import dx_City

from opencivicdata.core.models import Jurisdiction, Person, Organization, Membership, Post

from opencivicdata.legislative.models import Event, Bill, EventSource, EventLocation

from .models.models_base import UserAddedEvent, Comment, Apple, Quote, FBEvent


class FBEventSerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = FBEvent
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = Quote
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = Comment
        fields = '__all__'


class AppleSerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = Apple
        fields = '__all__'
        

############
## Events ##
############
class dxCitySerializer(serializers.ModelSerializer):
#    city_name = BaseCitySerializer()
    class Meta:
        model = dx_City
        fields = ('city_name',)


class JurisdictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jurisdiction
        fields = ('id', 'name')


class SourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSource
        fields = ('url',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = ('name',)


class EventSerializer(serializers.ModelSerializer):
    jurisdiction = JurisdictionSerializer()
    location = LocationSerializer()
    sources = SourcesSerializer(many=True)
#    city = dxCitySerializer()

    class Meta:
        model = Event
        fields = ('location', 'sources', 'name', 'start_date', 'description', 'jurisdiction',)
        depth = 1


class CreateEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAddedEvent
        fields = '__all__'
#        fields = ('id', 'name', 'event_type', 'location', 'city', 'startdate', 'link', 'description', 'participants', 'password', 'published')


        
###################
## Organizations ##
###################

class minPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'image',)
        depth = 1

        

class MembershipOrgSerializer(serializers.ModelSerializer):
    person = minPersonSerializer()
    class Meta:
        model = Membership
        fields = ('role', 'person',)


class minBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'identifier', 'title')
        depth = 1


class OrgMinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name' )
        

class OrganizationsSerializer(serializers.ModelSerializer):
#    person_members = BasePersonSerializer(many=True)
    memberships = MembershipOrgSerializer(many=True)
    jurisdiction = JurisdictionSerializer()
    parent = OrgMinSerializer()
#    posts = PostSerializer(many=True)    
    class Meta:
        model = Organization
        fields = ('id', 'name', 'image', 'classification', 'jurisdiction', 'memberships', 'parent', 'extras')
        

class OrgSerializer(serializers.ModelSerializer):
    bills = minBillSerializer(many=True)
    jurisdiction = JurisdictionSerializer()    
    memberships = MembershipOrgSerializer(many=True)
#    posts = PostSerializer(many=True)    
    class Meta:
        model = Organization
        fields = ('id', 'name', 'image', 'classification', 'memberships', 'jurisdiction', 'posts', 'bills', 'extras',)


        

###########
## Bill  ##
###########
        

class SponsorSerializer(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value.person, Person):
            s = minPersonSerializer(value.person)
            return s.data
        elif isinstance(value.organization, Organization):
            s = OrgSerializer(value.organization)
            return s.data
        else:
            pass


class BillSerializer(serializers.ModelSerializer):
    from_organization = OrgMinSerializer()
    sponsorships = SponsorSerializer(read_only=True, many=True)
    class Meta:
        model = Bill
        fields = ('id', 'identifier', 'sources', 'title', 'classification', 'subject', 'legislative_session', 'sponsorships', 'from_organization', 'actions')
        depth = 1


############
## Posts  ##
############
class PostSerializer(serializers.ModelSerializer):
    organization = OrgMinSerializer()
    class Meta:
        model = Post
        fields = ('id', 'label', 'role', 'organization')


class PostsSerializer(serializers.ModelSerializer):
    organization = OrgMinSerializer()
    class Meta:
        model = Post
        fields = ('id', 'label', 'role', 'organization')
        

################
## Membership ##
################
class MembershipSerializer(serializers.ModelSerializer):
    organization = OrgMinSerializer()
    post = PostSerializer()
    class Meta:
        model = Membership
        fields = ('id', 'organization', 'label', 'role', 'post',)


############
## Person ##
############
class PostPersonSerializer(serializers.ModelSerializer):
#    organization = OrgMinSerializer()
    class Meta:
        model = Post
        fields = ('label', 'role',)


class MembershipPersonSerializer(serializers.ModelSerializer):
    organization = OrgMinSerializer()
    post = PostPersonSerializer()
    class Meta:
        model = Membership
        fields = ('id', 'organization', 'label', 'role', 'post',)

        
class minMembershipSerializer(serializers.ModelSerializer):
    post = PostPersonSerializer()
    organization = OrgMinSerializer()
    class Meta:
        model = Membership
        fields = ('label', 'role', 'post', 'organization')


class BillSponsorSerializer(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value.bill, Bill):
            s = minBillSerializer(value.bill)
            return s.data
        else:
            pass


class PeopleSerializer(serializers.ModelSerializer):
    memberships = minMembershipSerializer(many=True)
    class Meta:
        model = Person
        fields = ('id', 'name', 'image', 'memberships',)
        depth = 1
        

class PersonSerializer(serializers.ModelSerializer):
    memberships = MembershipPersonSerializer(many=True)
    billsponsorship_set = BillSponsorSerializer(read_only=True, many=True)
    class Meta:
        model = Person
        fields = ('id', 'name', 'image', 'memberships', 'billsponsorship_set', 'contact_details', 'biography', 'extras', 'votes', 'biography', 'extras')
        depth = 1




##########
# Extras #
##########
        
"""        
class SponsorSerializer(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value.person, Person):
            s = PeopleSerializer(value.person)
            return s.data
        elif isinstance(value.organization, Organization):
            s = OrgSerializer(value.organization)
            return s.data
        else:
            pass
"""


"""        

        
class minPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
#        fields = '__all__'
        fields = ('id', 'name',)
        
"""

"""        
class minBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('identifier', 'sources', 'title', 'classification', 'subject', 'legislative_session',)
        depth = 1
        

        
"""
