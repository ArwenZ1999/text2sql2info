import sqlite3
import random
import string
from datetime import datetime
from faker import Faker
              
def generate_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_mock_data_agentParticipants():
    fake = Faker()
    mock_data = []
    i=0 
    while i< 50:
        full_name = fake.name()
        nickname = fake.name()[:3]
        login_name = random.choice(["jdoe123", "jdoe456", "bsmith789", "ajohnson101112"])
        deleted = random.choice([True, False])
        agent_id = "agent" + str(random.randint(1000,9999)) 
        pid = "pid" + str(random.randint(1000,9999))
        user_type = random.randint(0,2)
        user_type_name = ["System", "Human", "Bot"][user_type]
        role = random.choice(["admin", "user", "guest"])
        group_name = random.choice(["admins", "users", "guests"])
        group_id = random.randint(1000,9999)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        permission = random.choice(["READER", "ASSIGNED", "SUGGESTED_ASSIGNED_AGENT"])
        dialog_id = "dialog" + str(random.randint(1000,9999))
        
        data = (full_name, nickname, login_name, deleted, agent_id, pid, 
                user_type, user_type_name, role, group_name, group_id, time, 
                permission, dialog_id)
        
        mock_data.append(data)
        i += 1
    return mock_data

def generate_mock_data_campaign():
    fake = Faker()
    mock_data = []
    i=0
    while i< 50:
        campaign_id = "campaign" + str(random.randint(1000,9999))
        campaign_name = fake.sentence(nb_words=6)
        goal_id = "goal" + str(random.randint(1000,9999))
        goal_name = fake.sentence(nb_words=6)
        engagement_type = random.choice(["chat", "video", "phone", "email", "social", "web"])   
        visitor_profile_id = "visitorProfile" + str(random.randint(1000,9999))
        visitor_profile_name = fake.sentence(nb_words=6)
        lob_id = random.randint(1000,9999)
        lob_name = fake.sentence(nb_words=6)
        location_id = "location" + str(random.randint(1000,9999))
        location_name = fake.sentence(nb_words=6)
        behavior_system_default = random.choice([True, False])
        profile_system_default = random.choice([True, False])

        data=(campaign_id, campaign_name, 
              goal_id, goal_name, engagement_type, 
              visitor_profile_id, visitor_profile_name, lob_id, lob_name, 
              location_id, location_name, behavior_system_default, profile_system_default)
        mock_data.append(data)
        i += 1
    return mock_data

def generate_mock_data_consumerParticipants():
    fake = Faker()
    mock_data = []
    i=0
    while i< 50:
        participantId = "participant" + str(random.randint(1000,9999))
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        joinTime = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
        dialogId = "dialog" + str(random.randint(1000,9999))
        
        data = (participantId, time, joinTime, dialogId)
        
        mock_data.append(data)
        i += 1
    return mock_data


def generate_mock_data_interactions():
    fake = Faker()
    mock_data = []

    for i in range(50):
        interactionId = "interaction" + str(random.randint(1000,9999))
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        consumerId = "consumer" + str(random.randint(1000,9999))
        agentId = "agent" + str(random.randint(1000,9999))
        campaignId = "campaign" + str(random.randint(1000,9999))
        assignedAgentId = "agent" + str(random.randint(1000, 9999))
        assignedAgentFullName = fake.name()
        assignedAgentLoginName = fake.user_name()
        assignedAgentNickname = fake.first_name()
        interactionTime = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
        interactiveSequence = str(i)
        dialogId = "dialog" + str(random.randint(1000,9999))
        
        data = (interactionId, time, consumerId, agentId, campaignId, 
                assignedAgentId, assignedAgentFullName, assignedAgentLoginName, assignedAgentNickname, 
                interactionTime, interactiveSequence, dialogId)
        
        mock_data.append(data)

    return mock_data

       

if __name__ == "__main__":
    conn = sqlite3.connect('ConversationHistoryRecords.db')
    c = conn.cursor()
    mock_agentParticipants = generate_mock_data_agentParticipants()
    mock_campaign = generate_mock_data_campaign()
    mock_consumerParticipants=generate_mock_data_consumerParticipants()
    mock_interactions=generate_mock_data_interactions()
    c.executemany("INSERT INTO interactions VALUES (?,?,?,?,?,?,?,?,?,?,?)", mock_interactions)
    c.executemany("INSERT INTO consumerParticipants VALUES (?,?,?,?)", mock_consumerParticipants)
    c.executemany("INSERT INTO campaign VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", mock_campaign)
    c.executemany("INSERT INTO agentParticipants VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_agentParticipants)
    print('check here')
    conn.commit()
    conn.close()
