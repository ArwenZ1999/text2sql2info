'''Create data into the table agent
'''
conn.execute("""
    CREATE TABLE agent (
        time TEXT,
        assignedAgentId TEXT,
        targetSkillId INTEGER,  -- Note: Long changed to INTEGER 
        targetSkillName TEXT,
        reason TEXT,
        by TEXT,
        sourceSkillId INTEGER,  -- Note: Long changed to INTEGER
        sourceSkillName TEXT,
        sourceAgentId TEXT,
        sourceAgentFullName TEXT,
        sourceAgentLoginName TEXT,
        sourceAgentNickname  TEXT, 
        dialogId TEXT
    );
""")

conn.commit()  # Save the changes
print("Table 'agent' created successfully!")

sample_agent_data = [
    (
        "2023-11-19 10:22:11.123456",  
        "1234",
        5678,
        "Customer Service",
        "SuggestedAgentTimeout",
        '5678',
        9012,
        "Sales",
        "9012",
        "John Doe",
        "jdoe",
        "1234",  
        "123456"
    ),
    (
        "2023-11-20 11:33:22.654321",
        "2345",
        6789,
        "Sales",
        "AgentLogout",
        "6789",
        1234,
        "Customer Service",
        "1234",
        "Jane Doe",
        "jadoe",
        "2345",
        "234567"
    ),
    (
        "2023-11-21 12:44:33.987654",
        "3456",
        7890,
        "IT Support",
        "NewInteraction",  
        "7890",
        5678,
        "Sales",
        "5678",
        "Jim Smith",  
        "jismith",
        "3456",
        "345678"
    ),
    (
        "2023-11-22 13:55:44.321987",
        "4567",
        9012,
        "Customer Service",
        "AgentTimeout",
        "8901",
        2345,
        "IT Support",  
        "2345",
        "Jill Johnson",
        "jijohnson", 
        "4567",
        "456789"
    )
]


placeholders=",".join(["?"]*len(sample_agent_data[0]))
sql = f"INSERT INTO agent VALUES ({placeholders}*4)"
conn.executemany(sql,sample_agent_data)
conn.commit()

print("Sample data agent inserted!")


''' Create data into the table conversationhistoryrecords
'''
conn.execute('''CREATE TABLE conversationhistoryrecords
        (conversationId TEXT,
         customerId TEXT,
         startTime TEXT,
         endTime TEXT,
         duration INTEGER,
         firstName TEXT,
         surname TEXT,
         brand TEXT,
         latestAgentId TEXT,
         latestAgentNickname TEXT,
         latestAgentFullName TEXT,
         latestAgentLoginName TEXT,
         agentDeleted TEXT,
         latestSkillId TEXT,
         latestSkillName TEXT,
         source TEXT,
         closeReason TEXT,
         closeReasonDescription TEXT,
         mcs INTEGER,
         alertedMCS TEXT,
         status TEXT,
         fullDialogStatus TEXT,
         firstConversation Boolean,
         device TEXT, 
         browser TEXT,
         browserVersion TEXT,
         operatingSystem TEXT,
         operatingSystemVersion TEXT,
         latestAgentGroupId INTEGER,
         latestAgentGroupName TEXT,
         latestQueueState TEXT,
         isPartial TEXT,
         sessionId TEXT,
         interactionContextId TEXT,
         timeZone TEXT,
         features TEXT,
         language TEXT,
         integration TEXT,
         integrationVersion TEXT,
         appId TEXT,
         ipAddress TEXT,
         visitorId TEXT,
         latestHandlerAccountId TEXT,
         latestHandlerSkillId INTEGER)
         ''')
         
conn.commit()
print("conversationhistoryrecords table inserted!")

"""
add data for conversationhistoryrecords
"""
sample_data_converstaionhistory=[
('102',
 '103',
'2022-01-01 10:00:00',
 '2022-01-01 10:30:00',
 1800,
 'John',
 'Doe',
 'Acme',
 '1',
 'JohnD',
 'John Doe',
 'johnd',
 '0',
 '1',
 'Sales',
 'Web',
 'Timeout',
 'Call ended due to timeout',
 1,
 '0',
 'open',
 'active',
 True,
 'Desktop',
 'Chrome',
 '96.0',
 'Windows',
 '10',
 1,
 'Sales',
 'waiting',
 '0',
 '123',
 '456',
 'UTC',
 'chat,video',
 'en-US',
 'LivePerson',
 '8.3',
 '1234',
 '192.168.0.1',
 'abc123',
 '2',
 '1'),
('109',
 '104',
'2022-01-02 11:00:00',
 '2022-01-02 11:15:00',
 900,
 'Jane',
 'Smith',
 'Acme',
 '2',
 'JaneS',
 'Jane Smith',
 'janes',
 '0',
 '2',
 'Support',
 'Mobile App',
 'Resolved',
 'Issue resolved',
 0,
 '1',
 'closed',
 'done',
 False,
 'iOS',
 'Safari',
 '15.2',
 'iOS',
 '15.4',
 2,
 'Support',
 'routed',
 '0',
 '456',
 '789',
 'EST',
 'chat',
 'en-GB',
 'LivePerson',
 '8.3',
 '5678',
 '192.168.0.2',
 'def456',
 '3',
 '2'),
('180',
 '234',
'2022-01-03 12:00:00',
 '2022-01-03 12:15:00',
 900,
 'John',
 'Doe',
 'Contoso',
 '3',
 'JohnD',
 'John Doe',
 'johnd',
 '0',
 '3',
 'Sales',
 'Website',
 'Resolved',
 'Issue fixed',
 0,
 '2',
 'open',
 'in progress',
 False,
 'Chrome',
 '105.2',
 'Windows',
 '10',
 3,
 'Sales',
 'direct',
 '0',
 '987',
 '654',
 'PST',
 'web',
 'fr-FR',
 'LivePerson',
 '9.1',
 '91011',
 '192.168.0.3',
 'uvwxyz',
 '4',
 '3',
 '3'),
('0099',
 '8786',
'2022-01-04 09:30:00',
 '2022-01-04 09:45:00',
 900,
 'Jane',
 'Doe',
 'Fabrikam',
 '4',
 'JaneD',
 'Jane Doe',
 'janed',
 '0',
 '4',
 'Support',
 'Mobile App',
 'Unresolved',
 'Issue not fixed',
 0,
 '3',
 'pending',
 'waiting',
 True,
 'Android',
 'Chrome',
 '101.0',
 'Android',
 '12',
 4,
 'Support',
 'direct',
 '0',
 '123',
 '456',
 'CST',
 'app',
 'de-DE',
 'LivePerson',
 '9.2',
 '121314',
 '192.168.0.4',
 'stuvwx',
 '5',
 '4',)           
]
c = conn.cursor()
data = sample_data_converstaionhistory
placeholders=",".join(["?"]*len(sample_data_converstaionhistory[0]))
sql = f"INSERT INTO conversationhistoryrecords VALUES ({placeholders}*4)"
c.executemany(sql,data)
conn.commit()

"""
add data for campaign_engagement_data
"""
conn.execute('''CREATE TABLE campaign_engagement_data
              (campaignEngagementId TEXT, 
               campaignEngagementName TEXT,
               goalId TEXT,
               goalName TEXT,
               engagementSource TEXT,
               visitorBehaviorId TEXT,
               visitorBehaviorName TEXT,  
               visitorProfileId TEXT,
               visitorProfileName TEXT,
               lobId INTEGER,
               lobName TEXT,
               locationId TEXT,
               locationName TEXT,
               behaviorSystemDefault TEXT,
               profileSystemDefault TEXT)''')
sample_data_campaign_engagement = [
  ('ce001', 'Campaign 1', 'g001', 'Goal 1', 'Chat', 'vb001', 'Browse', 'vp001', 'Anonymous', 1, 'Insurance', 'loc001', 'New York', 'true', 'true'),
  ('ce002', 'Campaign 2', 'g002', 'Goal 2', 'Social', 'vb002', 'Purchase', 'vp002', 'Customer', 2, 'Banking', 'loc002', 'Chicago', 'false', 'false'),
  ('ce003', 'Campaign 3', 'g003', 'Goal 3', 'Email', 'vb003', 'Support', 'vp003', 'VIP', 3, 'Retail', 'loc003', 'Houston', 'true', 'false'),
  ('ce004', 'Campaign 4', 'g004', 'Goal 4', 'Phone', 'vb004', 'Learn', 'vp004', 'Lead', 4, 'Technology', 'loc004', 'Seattle', 'false', 'true')
]

c = conn.cursor()
placeholders = ",".join(["?"] * len(sample_data_campaign_engagement[0]))
sql = f"INSERT INTO campaign_engagement_data VALUES ({placeholders})"
c.executemany(sql, sample_data_campaign_engagement)
conn.commit()

import random
from faker import Faker
import sqlite3

# Connect to the database
conn = sqlite3.connect('ConversationHistoryRecords.db')
c = conn.cursor()

# Generate mock data for users table
fake = Faker()
for i in range(50):
    name = fake.name()
    email = fake.email()
    c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (name, email))

# Generate mock data for conversations table 
for i in range(50):
    user1_id = random.randint(1, 50)
    user2_id = random.randint(1, 50)
    while user1_id == user2_id:
        user2_id = random.randint(1, 50)
    topic = fake.sentence(nb_words=6)
    c.execute("INSERT INTO conversations VALUES (NULL, ?, ?, ?)", (user1_id, user2_id, topic))

# Generate mock data for messages table
for i in range(50):
    conversation_id = random.randint(1, 50)
    user_id = random.randint(1, 50)
    message = fake.paragraph(nb_sentences=3)
    c.execute("INSERT INTO messages VALUES (NULL, ?, ?, ?)", (conversation_id, user_id, message))

conn.commit()
conn.close()
