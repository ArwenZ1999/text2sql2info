import sqlite3
import random
import json
from datetime import datetime
from faker import Faker

def extract_dialogues(filepath):
    dialogues = []
    with open(filepath, 'r') as f:
        for line in f:
            data = json.loads(line)
            
            if 'dialogue' in data:
                dialogue = data['dialogue']
                dialogues.append(dialogue)
    utterances = []
    for dialogue in dialogues:
        utterances.extend(dialogue.split('\n'))   
    return utterances         

mock_dialogs=extract_dialogues('dialogsum/DialogSum_Data/dialogsum.dev.jsonl')
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
        visitorBehaviorId=random.randint(1000,9999)
        visitorBehaviorName=fake.sentence(nb_words=6)
        visitor_profile_id = "visitorProfile" + str(random.randint(1000,9999))
        visitor_profile_name = fake.sentence(nb_words=6)
        lob_id = random.randint(1000,9999)
        lob_name = fake.sentence(nb_words=6)
        location_id = "location" + str(random.randint(1000,9999))
        location_name = fake.sentence(nb_words=6)
        behavior_system_default = random.choice([True, False])
        profile_system_default = random.choice([True, False])

        data=(campaign_id, campaign_name, 
              goal_id, goal_name, engagement_type, visitorBehaviorId,visitorBehaviorName,
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
    i=0
    while i < 50:
        assignedAgentId="interaction" + str(random.randint(1000,9999))
        assignedAgentFullName = fake.name()
        assignedAgentLoginName = fake.user_name()
        assignedAgentNickname = fake.first_name()
        interactionTime = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
        interactiveSequence = str(i)
        dialogId = "dialog" + str(random.randint(1000,9999))
        
        data = (assignedAgentId, assignedAgentFullName, assignedAgentLoginName, assignedAgentNickname,
                interactionTime, interactiveSequence, dialogId)
        
        mock_data.append(data)
        i+=1
    return mock_data


def generate_mock_data_messageRecords():
    fake = Faker()

    mock_data = []
    i=0
    while i < 50:
        type_data= random.choice(["TEXT", "IMAGE", "VIDEO", "FILE"])
        text= random.choice(mock_dialogs)
        messageId = "message" + str(random.randint(1000,9999))
        dialogId = "dialog" + str(random.randint(1000,9999))
        participantId = random.randint(1000,9999)
        audience = random.choice(["AGENT", "CONSUMER"])
        seq = random.randint(1, 10)
        source = random.choice(["WEB", "MOBILE", "MESSENGER"])
        time = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
        integrationSource = random.choice(["FACEBOOK", "TWITTER", "WEBCHAT"])
        device = random.choice(["DESKTOP", "MOBILE", "TABLET"])
        sentBy = random.choice(["AGENT", "CONSUMER"])
        classifications = random.choice(['GREETING', 'QUESTION', 'ANSWER', 'ACTION'])
        
        data = (type_data,text, messageId, audience, seq, dialogId, participantId, source, time, integrationSource,device ,
                sentBy, classifications)
                
        mock_data.append(data)
        i+=1
    return mock_data



def generate_mock_data_messageScores():
    i=0   
    fake=Faker()
    mock_data = []
    while i< 50:
        messageId = "message" + str(random.randint(1000,9999))
        messageRawScore = random.randint(0, 100)
        mcs = random.randint(0, 100)
        time = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
        data = (messageId, messageRawScore, mcs, time)
        mock_data.append(data)
        i+=1
    
    return mock_data


def generate_mock_data_messageStatuses():
  fake = Faker()
  
  mock_data = []
  i=0
  while i<50:
    messageId = "message" + str(random.randint(1000,9999))
    seq = random.randint(1, 10)
    dialogId = "dialog" + str(random.randint(1000,9999))  
    time = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S.%f")
    participantId = str(random.randint(1000,9999))
    participantType = random.choice(["AGENT", "CONSUMER"])
    messageDeliveryStatus = random.choice(["sent", "accepted", "read"])
    
    data = (messageId, seq, dialogId, time, participantId, participantType, messageDeliveryStatus)
            
    mock_data.append(data)
    i+=1

  return mock_data


def generate_mock_data_recordsInfo():
  i=0
  mock_data = []
  fake=Faker()
  while i <50 :
    conversationId = fake.uuid4()
    customerId = str(random.randint(100000, 999999))
    startTime = fake.date_time(end_datetime="-1y")
    endTime = fake.date_time_ad(start_datetime=startTime) 

    duration = random.randint(60, 3600)
    firstName = fake.first_name()
    surname = fake.last_name()
    brand = random.choice(["Halifax", "Lloyds", "BoS", "MBNA"])
    latestAgentId = str(random.randint(100000, 999999))
    latestAgentNickname = fake.user_name() 
    latestAgentFullName = fake.name()
    latestAgentLoginName = fake.user_name()
    agentDeleted = random.choice(["true", "false"])
    latestSkillId = str(random.randint(1000, 9999))
    latestSkillName = fake.job()
    source = random.choice(["Mobile", "Web", "App"])
    closeReason = random.choice(["agent", "customer"])
    closeReasonDescription = fake.sentence(nb_words=10)
    mcs = random.randint(0, 100)
    alertedMCS = random.choice(["Positive", "Neutral", "Negative"])
    status = random.choice(["open", "closed"])
    fullDialog = random.choice(["true", "false"])
    firstConversation = random.choice(["true", "false"])
    device = random.choice(["Desktop", "Mobile", "Tablet"])
    browser = random.choice(["chrome", "safari", "bing", "firefox"])
    browserVersion = random.choice(["1.10", "2.20", "4.40", "5.50"])
    operatingSystem = random.choice(["Windows", "Mac", "Linux", "iOS", "Android"])
    operatingSystemVersion = fake.lexify(text="????.??.?")
    latestAgentGroupld = random.randint(1000, 9999)
    latestAgentGroupName = fake.job()
    latestQueueState = random.choice(["assigned", "waiting"]) 
    isPartial = random.choice(["true", "false"])
    sessionid = fake.uuid4()
    interactionContextid = fake.uuid4()
    timeZone = fake.timezone()
    features = random.sample(["feature1", "feature2", "feature3"], random.randint(1,3))
    language = fake.locale()
    integration = random.choice(["mobile-sdk", "web-sdk", "brand-sdk"])
    integrationVersion = fake.lexify(text="?.?.?")
    appld = fake.user_name()
    ipAddress = fake.ipv4() 
    visitorld = fake.uuid4()
    latestHandlerAccountla = str(random.randint(100000, 999999))
    latestHandlerSkillld = random.randint(1000, 9999)
    
    data = (conversationId, customerId, startTime, endTime, duration, firstName, 
            surname, brand, latestAgentId, latestAgentNickname, latestAgentFullName,
            latestAgentLoginName, agentDeleted, latestSkillId, latestSkillName, 
            source, closeReason, closeReasonDescription, mcs, alertedMCS, status, 
            fullDialog, firstConversation, device, browser, browserVersion, operatingSystem,
            operatingSystemVersion, latestAgentGroupld, latestAgentGroupName, latestQueueState, 
            isPartial, sessionid, interactionContextid, timeZone, str(features), language, 
            integration, integrationVersion, appld, ipAddress, visitorld, latestHandlerAccountla, 
            latestHandlerSkillld)
    
    mock_data.append(data)
    i+=1

  return mock_data

def generate_mock_data_transfers():
    fake = Faker()
    i=0
    mock_transfers = []
    while i<50:
        curationTime = fake.date_time()
        assignedAgentId = fake.random_number(digits=5)
        targetSkillId = random.randint(1000, 9999)
        targetSkillName = fake.job()
        reason = random.choice(["back2Q", "Agent", "SuggestedAgentTimeout", "Skill", "TakeOver"])
        by = random.randint(100000, 999999)
        sourceSkillId = str(random.randint(1000, 9999))
        sourceSkillName = fake.job() 
        sourceAgentId = fake.random_number(digits=5)
        sourceAgentFullName = fake.name()
        sourceAgentLoginName = fake.user_name()
        sourceAgentNickname = random.randint(100000, 999999)
        dialogId = fake.uuid4()
        
        data = (curationTime, assignedAgentId, targetSkillId, targetSkillName, reason, by, 
                sourceSkillId, sourceSkillName, sourceAgentId, sourceAgentFullName, 
                sourceAgentLoginName, sourceAgentNickname, dialogId)
                
        mock_transfers.append(data)
        i+=1
    return mock_transfers


if __name__ == "__main__":
    conn = sqlite3.connect('ConversationHistoryRecords.db')
    c = conn.cursor()
    mock_agentParticipants = generate_mock_data_agentParticipants()
    mock_campaign = generate_mock_data_campaign()
    mock_consumerParticipants=generate_mock_data_consumerParticipants()
    mock_interactions=generate_mock_data_interactions()
    mock_messageRecords=generate_mock_data_messageRecords()
    mock_messageScores=generate_mock_data_messageScores()
    mock_messageStatuses=generate_mock_data_messageStatuses()
    mock_recordsinfo=generate_mock_data_recordsInfo()
    mock_transfers=generate_mock_data_transfers()
    c.executemany("INSERT INTO transfers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_transfers)
    c.executemany("INSERT INTO recordsInfo VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_recordsinfo)
    c.executemany("INSERT INTO messageStatuses VALUES (?,?,?,?,?,?,?)", mock_messageStatuses)
    c.executemany("INSERT INTO messageScores VALUES (?,?,?,?)", mock_messageScores)
    c.executemany("INSERT INTO messageRecords VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_messageRecords)
    c.executemany("INSERT INTO interactions VALUES (?,?,?,?,?,?,?)", mock_interactions)
    c.executemany("INSERT INTO consumerParticipants VALUES (?,?,?,?)", mock_consumerParticipants)
    c.executemany("INSERT INTO campaign VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_campaign)
    c.executemany("INSERT INTO agentParticipants VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", mock_agentParticipants)
    print('Data crete successful!')
    conn.commit()
    conn.close()
