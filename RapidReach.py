import tkinter as tk
from tkinter import font as tkfont

# =====================
# DATA
# =====================

CATEGORIES = [
    (1, "🚑  Ambulance / Medical Services"),
    (2, "🚔  Police / Law Enforcement"),
    (3, "🚒  Fire Brigade / Rescue"),
    (4, "🌊  Disaster & Rescue Services"),
    (5, "🛣️  Motorway & Transport Authorities"),
    (6, "🤝  Social Protection Helplines"),
    (7, "🐾  Animal & Specialized Services"),
    (8, "⚡  Utility & Infrastructure Services"),
]

SUBS = {
    1: [
        "Cardiac Arrest / Heart Attack",
        "Respiratory Distress / Choking",
        "Poisoning & Overdose",
        "Snake or Insect Bites",
        "Road Traffic Accident (RTA)",
        "Blood Bank & Organ Donation",
        "Mental Health & Suicide Prevention",
    ],
    2: [
        "Theft / Armed Robbery",
        "Cyber Crime & Online Fraud",
        "Missing Persons / Amber Alert",
        "Domestic Violence",
        "Terrorism / Suspicious Activity",
        "Workplace Harassment",
    ],
    3: [
        "Fire Emergency",
        "Forest Fires",
        "Chemical Spills",
        "Gas Leakage",
        "Electrical Short Circuit / Fallen Wires",
        "Structure Collapse / Building Fall",
    ],
    4: [
        "Flood & Water Logging",
        "Earthquake Response",
        "Large-Scale Building Collapse",
        "Water Rescue / Drowning",
    ],
    5: [
        "Highway / Motorway Breakdown",
        "Road Traffic Accident (RTA)",
        "Railway Emergency",
        "Airport / Aviation Security",
        "Elevator / Lift Malfunction",
    ],
    6: [
        "Women Helpline / Domestic Violence / Harassment",
        "Child Protection / Child Abuse",
        "Missing Child",
        "Elderly Care Services",
    ],
    7: [
        "Animal Cruelty & Rescue",
        "Dead Body Transport / Mortuary Services",
    ],
    8: [
        "Major Water Leakage",
        "Sewerage Overflow / Blockage",
        "Total Power Grid Failure",
        "Gas Supply Emergency",
    ],
}

INFO = {
    (1, 1): {
        "title": "Cardiac Arrest / Heart Attack",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Check the area is safe before approaching.", False),
            ("Tap the person and shout to check if they respond.", False),
            ("If no response, call 1122 / 115 immediately or ask someone to call.", False),
            ("Check breathing for up to 10 seconds.", False),
            ("If not breathing or only gasping, start CPR immediately.", False),
            ("Lay the person flat on a firm surface.", False),
            ("Place one hand in the center of the chest, other on top.", False),
            ("Keep arms straight and press hard and fast.", False),
            ("Push at least 2 inches deep at 100–120 compressions per minute.", False),
            ("Allow chest to fully rise between compressions.", False),
            ("If trained, give 2 breaths after every 30 compressions.", False),
            ("If not trained, continue hands-only CPR.", False),
            ("Use an AED immediately if available and follow its instructions.", False),
            ("Continue CPR until help arrives or the person starts breathing.", False),
            ("Do not stop CPR unless absolutely necessary.", False),
            ("Do not give food, water, or medication.", False),
        ],
    },
    (1, 2): {
        "title": "Respiratory Distress / Choking",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Check if the person can speak, cough, or breathe.", False),
            ("If they can cough, encourage strong coughing.", False),
            ("If breathing becomes difficult, call 1122 / 115 immediately.", False),
            ("If unable to speak or breathe, treat as severe choking.", False),
            ("Stand behind the person and wrap your arms around their waist.", False),
            ("Make a fist and place it above the navel.", False),
            ("Grasp your fist with the other hand.", False),
            ("Give quick inward and upward thrusts (Heimlich maneuver).", False),
            ("Repeat until object is expelled or person becomes unconscious.", False),
            ("If the person becomes unconscious, gently lower them to the ground.", False),
            ("Start CPR immediately and check airway between compressions.", False),
            ("For infants, use back blows and chest thrusts (not abdominal thrusts).", False),
            ("Do not put fingers blindly into the mouth.", False),
            ("Do not give food or water during choking.", False),
        ],
    },
    (1, 3): {
        "title": "Poisoning & Overdose",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Call 1122 / 115 immediately.", False),
            ("Check if the person is conscious and breathing.", False),
            ("If unconscious but breathing, place in recovery position.", False),
            ("If not breathing, start CPR if trained.", False),
            ("Identify the poison if possible (medicine, chemical, gas).", False),
            ("Keep bottle, packet, or label to show medical staff.", False),
            ("If swallowed poison, do NOT induce vomiting unless told by professionals.", False),
            ("If inhaled gas, move the person to fresh air immediately.", False),
            ("If poison on skin, remove contaminated clothing.", False),
            ("Wash affected skin with clean water.", False),
            ("Keep the person calm and still.", False),
            ("Stay with them until help arrives.", False),
            ("Do not give food, drink, or medicine unless advised.", False),
            ("Do not delay seeking help.", False),
        ],
    },
    (1, 4): {
        "title": "Snake or Insect Bites",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Call 1122 / 115 immediately.", False),
            ("Keep the person calm and still.", False),
            ("Limit movement to slow the spread of venom.", False),
            ("Keep the bitten area at or below heart level.", False),
            ("Remove rings, watches, or tight clothing before swelling starts.", False),
            ("Clean the bite gently with water if possible.", False),
            ("Cover with a clean, loose bandage.", False),
            ("Note the time of the bite and symptoms.", False),
            ("If safe, remember the snake/insect appearance (do not try to catch it).", False),
            ("Watch for signs like swelling, pain, breathing difficulty, or dizziness.", False),
            ("Do not cut the wound or suck out venom.", False),
            ("Do not apply ice or chemicals.", False),
            ("Do not tie a tight tourniquet.", False),
            ("Do not give food, alcohol, or unnecessary medicine.", False),
        ],
    },
    (1, 5): {
        "title": "Road Traffic Accident (RTA)",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Ensure your own safety before helping others.", False),
            ("Move to a safe area away from traffic.", False),
            ("Call 1122 / 115 immediately and give exact location.", False),
            ("Turn on hazard lights or warn approaching vehicles.", False),
            ("Do not rush into traffic without checking surroundings.", False),
            ("Check injured persons for consciousness and breathing.", False),
            ("Do not move seriously injured people unless there is fire or danger.", False),
            ("If bleeding heavily, apply firm pressure with cloth or bandage.", False),
            ("Keep injured person still and calm.", False),
            ("If unconscious but breathing, place in recovery position.", False),
            ("If not breathing, start CPR if trained.", False),
            ("Do not remove helmets unless necessary for breathing.", False),
            ("Do not give food, water, or medication.", False),
            ("Stay at the scene until emergency services arrive.", False),
        ],
    },
    (1, 6): {
        "title": "Blood Bank & Organ Donation",
        "contacts": ["1122 / 115  –  Emergency Rescue"],
        "steps": [
            ("Call 1122 / 115 or contact the hospital immediately.", False),
            ("Confirm the required blood group and number of units.", False),
            ("Contact nearby blood banks or hospital transfusion services.", False),
            ("Ask family, friends, or verified donors for urgent help.", False),
            ("Share patient details: name, hospital, blood group, urgency.", False),
            ("Keep doctor's prescription or hospital slip ready.", False),
            ("Ensure donor is healthy and meets basic donation criteria.", False),
            ("Follow hospital instructions for safe blood donation.", False),
            ("For organ donation, inform hospital staff immediately.", False),
            ("Consent from family/legal guardians is required.", False),
            ("Do not trust unknown or illegal paid donors.", False),
            ("Do not delay in arranging blood in emergencies.", False),
        ],
    },
    (1, 7): {
        "title": "Mental Health & Suicide Prevention",
        "contacts": ["1122 / 115  –  Emergency Rescue", "15  –  Police"],
        "steps": [
            ("Stay with the person and ensure immediate safety.", False),
            ("Speak calmly and listen without judging or arguing.", False),
            ("Encourage them to talk about how they feel.", False),
            ("Remove sharp objects, medicines, or harmful items nearby.", False),
            ("If risk is serious, call 1122 / 115 or Police 15 immediately.", False),
            ("Reassure them that help is available and they are not alone.", False),
            ("Encourage contacting a trusted family member or friend.", False),
            ("Keep them in a safe and comfortable place.", False),
            ("Stay until professional help arrives.", False),
            ("Do not leave the person alone if suicide risk is high.", False),
            ("Do not ignore warning signs or delay seeking help.", False),
            ("Do not argue, threaten, or judge the person.", False),
        ],
    },
    (2, 1): {
        "title": "Theft / Armed Robbery",
        "contacts": ["15  –  Police"],
        "steps": [
            ("Stay calm and do not resist if the robber is armed.", False),
            ("Hand over valuables if demanded.", False),
            ("Avoid sudden movements or arguing.", False),
            ("Try to stay observant without staring directly.", False),
            ("Notice details like face, clothing, voice, or vehicle.", False),
            ("Move to a safe place as soon as possible.", False),
            ("Call Police 15 immediately.", False),
            ("Note the time, location, and direction the suspect escaped.", False),
            ("Warn others nearby if safe to do so.", False),
            ("Secure doors/area after the incident if applicable.", False),
            ("Cooperate fully with police when they arrive.", False),
            ("Do not chase the suspect.", False),
            ("Do not disturb the crime scene or touch evidence.", False),
        ],
    },
    (2, 2): {
        "title": "Cyber Crime & Online Fraud",
        "contacts": ["1799  –  Cyber Crime"],
        "steps": [
            ("Do not share OTP, PIN, passwords, or bank details with anyone.", False),
            ("Stop communication with the suspected scammer immediately.", False),
            ("Take screenshots of messages, numbers, links, and transactions.", False),
            ("Save all evidence (emails, receipts, call logs).", False),
            ("Contact your bank or mobile wallet to block transactions.", False),
            ("Change passwords of affected accounts immediately.", False),
            ("Enable two-factor authentication if available.", False),
            ("Report the incident to Cyber Crime helpline 1799.", False),
            ("Inform a trusted person if large money or sensitive data is involved.", False),
            ("Do not click unknown links or download suspicious files.", False),
            ("Do not delete evidence before reporting.", False),
        ],
    },
    (2, 3): {
        "title": "Missing Persons",
        "contacts": ["15  –  Police"],
        "steps": [
            ("Call Police 15 immediately; do not wait.", False),
            ("Share recent photo, clothing, age, and last seen location.", False),
            ("Check nearby places: home, school, workplace, relatives.", False),
            ("Contact friends, neighbors, and known contacts.", False),
            ("Visit or call nearby hospitals and police stations.", False),
            ("Ask nearby shops/buildings for CCTV footage if available.", False),
            ("Keep your phone available for police contact.", False),
            ("Stay at last known location if advised by authorities.", False),
            ("Do not delay reporting or assume they will return quickly.", False),
        ],
    },
    (2, 4): {
        "title": "Domestic Violence",
        "contacts": ["15  –  Police", "1099  –  Women Helpline"],
        "steps": [
            ("If in immediate danger, call Police 15 right away.", False),
            ("Move to a safe place or public area if possible.", False),
            ("Contact Women Helpline 1099 for support and guidance.", False),
            ("Inform a trusted friend, family member, or neighbor.", False),
            ("Keep important items ready: phone, ID, money, essentials.", False),
            ("Save evidence: photos, messages, medical reports.", False),
            ("Plan a safe way to leave if the situation worsens.", False),
            ("Stay in a place where help is easily accessible.", False),
            ("Do not confront the abuser alone.", False),
            ("Do not stay in a situation where your life is at risk.", False),
        ],
    },
    (2, 5): {
        "title": "Suspicious Activity / Terrorism",
        "contacts": ["15  –  Police"],
        "steps": [
            ("Move away from the area calmly without creating panic.", False),
            ("Call Police 15 and report the exact location.", False),
            ("Observe from a safe distance if needed.", False),
            ("Note details: person, behavior, object, vehicle, timing.", False),
            ("Warn others nearby if it can be done safely.", False),
            ("Follow instructions from police or security personnel.", False),
            ("Keep emergency exits in mind and stay alert.", False),
            ("Do not touch or approach suspicious objects or bags.", False),
            ("Do not spread rumors or panic messages.", False),
            ("Do not ignore unusual or threatening behavior.", False),
        ],
    },
    (2, 6): {
        "title": "Workplace Harassment",
        "contacts": ["15  –  Police"],
        "steps": [
            ("Stay calm and remove yourself from the situation if possible.", False),
            ("Clearly tell the person to stop if it is safe to do so.", False),
            ("Document incidents: dates, times, messages, and witnesses.", False),
            ("Save evidence such as emails, chats, recordings, or photos.", False),
            ("Report the issue to HR, supervisor, or relevant authority.", False),
            ("Inform a trusted colleague or friend for support.", False),
            ("If there are threats, stalking, or assault, call Police 15 immediately.", False),
            ("Avoid being alone with the person if you feel unsafe.", False),
            ("Do not ignore repeated behavior.", False),
            ("Do not meet the harasser alone in isolated places.", False),
        ],
    },
    (3, 1): {
        "title": "Fire Emergency",
        "contacts": ["16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Call 16 / 1122 immediately and give exact location.", False),
            ("Alert others and start evacuation calmly.", False),
            ("Use stairs only — never use elevators.", False),
            ("Stay low to avoid smoke and cover nose/mouth with cloth.", False),
            ("Move quickly to the nearest safe exit.", False),
            ("If possible, close doors behind you to slow fire spread.", False),
            ("Help children, elderly, or injured people first if safe.", False),
            ("Once outside, move to a safe distance from the building.", False),
            ("Do not re-enter the building for any reason.", False),
            ("If clothes catch fire: Stop, Drop, and Roll.", False),
            ("Do not hide inside rooms or bathrooms.", False),
        ],
    },
    (3, 2): {
        "title": "Forest Fires",
        "contacts": ["16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Move away from the fire immediately to a safe area.", False),
            ("Call 16 / 1122 and report the exact location.", False),
            ("Cover nose and mouth with a cloth to reduce smoke inhalation.", False),
            ("Move upwind (away from direction of smoke/fire) if possible.", False),
            ("Do not try to fight large fires yourself.", False),
            ("Evacuate early if fire is spreading quickly.", False),
            ("Assist children, elderly, or injured people if safe.", False),
            ("Keep vehicle windows closed while evacuating by road.", False),
            ("Stay on cleared roads and avoid entering forest paths.", False),
            ("Do not stop to take photos or videos.", False),
            ("Do not return to the affected area until declared safe.", False),
        ],
    },
    (3, 3): {
        "title": "Chemical Spills",
        "contacts": ["16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Leave the area immediately if you smell or see a chemical spill.", False),
            ("Move upwind and away from the spill location.", False),
            ("Warn others nearby without creating panic.", False),
            ("Call 16 / 1122 and report location and type of spill if known.", False),
            ("Avoid touching, inhaling, or stepping into the chemical.", False),
            ("Cover nose and mouth with cloth if exposed to fumes.", False),
            ("Remove contaminated clothing if safe to do so.", False),
            ("Wash exposed skin with clean water if available.", False),
            ("Keep a safe distance until emergency teams arrive.", False),
            ("Do not try to clean or neutralize the chemical yourself.", False),
            ("Do not assume all spills are harmless.", False),
        ],
    },
    (3, 4): {
        "title": "Gas Leakage",
        "contacts": ["16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Do NOT switch on or off any electrical switches or appliances.", False),
            ("Do NOT use matches, lighters, candles, or open flames.", False),
            ("Open doors and windows slowly to ventilate the area.", False),
            ("Turn off the main gas valve if it is safe to do so.", False),
            ("Evacuate the area immediately and move to a safe distance.", False),
            ("Warn others nearby calmly.", False),
            ("Call 16 / 1122 from outside the affected area.", False),
            ("Avoid using mobile phones inside the leak area.", False),
            ("Do not create sparks (including plugs, chargers, switches).", False),
            ("Stay outside until authorities declare the area safe.", False),
        ],
    },
    (3, 5): {
        "title": "Electrical Short Circuit / Fallen Wires",
        "contacts": ["16 / 1122  –  Fire Brigade", "WAPDA / Electricity Board"],
        "steps": [
            ("Stay far away from fallen wires or sparks.", False),
            ("Warn others to keep a safe distance.", False),
            ("Do NOT touch any wire, pole, or electrical device.", False),
            ("Do NOT attempt to remove fallen wires yourself.", False),
            ("Turn off main power only if it is safe and accessible.", False),
            ("Keep water and metal objects away from the area.", False),
            ("If someone is shocked, do NOT touch them until power is off.", False),
            ("Call 16 / 1122 and report exact location immediately.", False),
            ("Inform electricity authority (WAPDA/LESCO) if available.", False),
            ("Keep children and crowd away from the site.", False),
            ("Stay alert for sparks or fire risk.", False),
            ("Do not use water on electrical fire.", False),
        ],
    },
    (3, 6): {
        "title": "Structure Collapse / Building Fall",
        "contacts": ["16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Move away from the collapsed building immediately.", False),
            ("Warn others to stay clear of the area.", False),
            ("Call 16 / 1122 and report exact location and possible trapped people.", False),
            ("Do NOT enter unstable structures.", False),
            ("If you are trapped, stay still and avoid kicking up dust.", False),
            ("Cover nose and mouth with cloth or mask.", False),
            ("Tap on pipes or walls to signal rescuers.", False),
            ("Shout only when necessary to conserve energy.", False),
            ("Keep roads and access points clear for rescue teams.", False),
            ("Do NOT attempt to move heavy debris yourself.", False),
            ("Do NOT re-enter collapsed or cracked structures.", False),
        ],
    },
    (4, 1): {
        "title": "Flood & Water Logging",
        "contacts": ["051-111-157-157  –  NDMA", "1129  –  PDMA Punjab", "1736  –  PDMA Sindh"],
        "steps": [
            ("Move to higher ground immediately.", False),
            ("Follow official warnings and evacuation instructions.", False),
            ("Avoid walking or driving through floodwater.", False),
            ("Even shallow water can be dangerous or contaminated.", False),
            ("Switch off electricity and gas supply if it is safe.", False),
            ("Do NOT touch electrical devices in water.", False),
            ("Keep children, elderly, and animals away from floodwater.", False),
            ("Take essential items: ID, medicine, phone, water.", False),
            ("Stay away from bridges, drains, and fast-flowing water.", False),
            ("Do NOT return to flooded areas until declared safe.", False),
        ],
    },
    (4, 2): {
        "title": "Earthquake Response",
        "contacts": ["051-111-157-157  –  NDMA", "1129  –  PDMA Punjab", "1736  –  PDMA Sindh"],
        "steps": [
            ("Drop to the ground immediately.", False),
            ("Take Cover under a sturdy table or against an interior wall.", False),
            ("Hold On until shaking stops.", False),
            ("Stay away from windows, glass, and heavy furniture.", False),
            ("If outside, move to open ground away from buildings and wires.", False),
            ("If driving, stop safely and stay inside the vehicle.", False),
            ("After shaking stops, evacuate carefully using stairs only.", False),
            ("Check yourself and others for injuries.", False),
            ("Be alert for aftershocks.", False),
            ("Do NOT use elevators.", False),
            ("Avoid damaged buildings and fallen wires.", False),
            ("Do NOT re-enter structures until declared safe.", False),
        ],
    },
    (4, 3): {
        "title": "Large-Scale Building Collapse",
        "contacts": ["1122  –  Emergency Rescue", "051-111-157-157  –  NDMA"],
        "steps": [
            ("Move away from the collapsed structure immediately.", False),
            ("Warn others to stay clear of the area.", False),
            ("Call 1122 and report exact location and possible trapped people.", False),
            ("Do NOT enter unstable or partially collapsed buildings.", False),
            ("Do NOT attempt to move heavy debris yourself.", False),
            ("Keep access routes clear for rescue vehicles.", False),
            ("If you are trapped:", False),
            ("Stay calm and conserve energy.", False),
            ("Cover nose and mouth to avoid dust inhalation.", False),
            ("Tap on pipes or walls or shout periodically to signal rescuers.", False),
            ("Avoid unnecessary movement to prevent further collapse.", False),
            ("Do NOT light matches or create sparks.", False),
            ("Do NOT panic or make random loud movements constantly.", False),
        ],
    },
    (4, 4): {
        "title": "Water Rescue / Drowning",
        "contacts": ["1122  –  Emergency Rescue"],
        "steps": [
            ("Call 1122 immediately and give exact location.", False),
            ("Do NOT jump into water unless you are trained and it is safe.", False),
            ("Try to rescue from land first using a rope, stick, or floating object.", False),
            ("Encourage the person to grab onto something that floats.", False),
            ("If the person is unconscious and brought out of water:", False),
            ("Check breathing immediately.", False),
            ("If not breathing, start CPR if trained.", False),
            ("Continue CPR until emergency help arrives.", False),
            ("Keep the person warm and dry after rescue.", False),
            ("Do NOT delay calling for help.", False),
            ("Do NOT attempt risky water entry without equipment or training.", False),
        ],
    },
    (5, 1): {
        "title": "Highway / Motorway Breakdown",
        "contacts": ["130  –  Motorway Police"],
        "steps": [
            ("Turn on hazard lights immediately.", False),
            ("Slow down and move vehicle to the hard shoulder or emergency lane.", False),
            ("Keep passengers inside or move them behind safety barriers if available.", False),
            ("Exit vehicle only when it is safe to do so.", False),
            ("Place warning triangle or reflectors behind the vehicle if available.", False),
            ("Call 130 and give location (motorway name, direction, km marker, nearest exit).", False),
            ("Stay away from moving traffic.", False),
            ("Do NOT stand on the road side of the vehicle.", False),
            ("Wait for help inside a safe area away from traffic.", False),
            ("Keep emergency numbers and vehicle details ready.", False),
        ],
    },
    (5, 2): {
        "title": "Road Traffic Accident (RTA)",
        "contacts": ["1122 / 130 / 15  –  Emergency Services"],
        "steps": [
            ("Ensure your own safety before approaching the scene.", False),
            ("Turn on hazard lights and warn oncoming traffic.", False),
            ("Call 1122 / 130 / 15 and give exact location.", False),
            ("State number of injured and type of accident if possible.", False),
            ("Do NOT move seriously injured people unless there is fire or immediate danger.", False),
            ("Check breathing and consciousness of victims.", False),
            ("Control bleeding using firm pressure with clean cloth.", False),
            ("Keep injured person still and calm.", False),
            ("If unconscious but breathing, place in recovery position.", False),
            ("If not breathing and trained, start CPR immediately.", False),
            ("Do NOT remove helmets unless breathing is blocked.", False),
            ("Do NOT give food, water, or medication.", False),
            ("Stay at the scene until emergency services arrive.", False),
        ],
    },
    (5, 3): {
        "title": "Railway Emergency",
        "contacts": ["117  –  Railway Helpline", "15  –  Police"],
        "steps": [
            ("Move away from tracks immediately.", False),
            ("Warn others to stay clear of railway lines.", False),
            ("Call 117 or 15 and report exact location (station, track, direction).", False),
            ("Do NOT stand or walk on tracks at any time.", False),
            ("Do NOT try to stop or block a moving train.", False),
            ("If someone is injured near tracks, avoid rushing in.", False),
            ("Wait for railway staff or emergency responders.", False),
            ("Follow instructions from railway authorities or police.", False),
            ("Keep children and crowd away from the area.", False),
            ("If there is an accident, stay at a safe distance from trains and wires.", False),
            ("Do NOT touch electrical railway lines or equipment.", False),
        ],
    },
    (5, 4): {
        "title": "Airport / Aviation Security",
        "contacts": ["114  –  ASF (Airport Security Force)", "15  –  Police"],
        "steps": [
            ("Inform airport security immediately if you notice suspicious activity.", False),
            ("Move away from any unattended bags or suspicious objects.", False),
            ("Call 114 or 15 and report exact location inside the airport.", False),
            ("Follow all instructions from airport security staff.", False),
            ("Keep calm and avoid creating panic.", False),
            ("Keep your ID and travel documents ready if asked.", False),
            ("Stay in designated safe or waiting areas.", False),
            ("Do NOT touch or move unattended luggage.", False),
            ("Do NOT spread rumors or unverified information.", False),
            ("Be alert but do not interfere with security operations.", False),
        ],
    },
    (5, 5): {
        "title": "Elevator / Lift Malfunction",
        "contacts": ["Building Security / Maintenance"],
        "steps": [
            ("Stay calm and do not panic.", False),
            ("Press the emergency alarm or help button.", False),
            ("Call building security or maintenance immediately.", False),
            ("Share location: building name, floor, and lift number.", False),
            ("Use the intercom if available to communicate.", False),
            ("Do NOT try to force open lift doors.", False),
            ("Do NOT attempt to climb out unless instructed by professionals.", False),
            ("Wait calmly inside the lift until help arrives.", False),
            ("If phone signal is available, call emergency contacts.", False),
            ("Keep children and others calm and seated if possible.", False),
            ("Do NOT jump or force movement inside the lift.", False),
        ],
    },
    (6, 1): {
        "title": "Women Helpline / Domestic Violence / Harassment",
        "contacts": ["15  –  Police", "1099  –  Women Helpline"],
        "steps": [
            ("If in immediate danger, call Police 15 right away.", False),
            ("Move to a safe place or public area if possible.", False),
            ("Contact Women Helpline 1099 for guidance and support.", False),
            ("Inform a trusted friend, family member, or neighbor.", False),
            ("Keep your phone charged and accessible.", False),
            ("Save evidence such as messages, calls, photos, or threats.", False),
            ("Avoid being alone with the threatening person.", False),
            ("Do NOT ignore repeated harassment or threats.", False),
            ("If possible, plan a safe exit route from the situation.", False),
            ("Stay in contact with someone you trust until safe.", False),
        ],
    },
    (6, 2): {
        "title": "Child Protection / Child Abuse",
        "contacts": ["1121  –  Child Protection", "15  –  Police", "1122  –  Emergency Rescue"],
        "steps": [
            ("If the child is in immediate danger, call 1122 or 15 right away.", False),
            ("Move the child to a safe and calm environment if possible.", False),
            ("Contact Child Protection Helpline 1121 immediately.", False),
            ("Inform a trusted adult, guardian, or authority.", False),
            ("If the child is injured, seek medical help immediately.", False),
            ("Keep the child calm and reassure them.", False),
            ("Listen carefully and do not blame or pressure the child.", False),
            ("Preserve any evidence if safe (messages, injuries, details).", False),
            ("Do NOT confront the suspected abuser alone if it increases risk.", False),
            ("Do NOT ignore signs of abuse or delay reporting.", False),
            ("Stay with the child or ensure a trusted person stays with them.", False),
        ],
    },
    (6, 3): {
        "title": "Missing Child",
        "contacts": ["15  –  Police", "1121  –  Child Protection"],
        "steps": [
            ("Call Police 15 and Child Protection 1121 immediately.", False),
            ("Do NOT wait; report as soon as the child is missing.", False),
            ("Share recent photo, age, clothing, and physical description.", False),
            ("Provide last seen location and time.", False),
            ("Check nearby safe places (home, school, relatives, friends).", False),
            ("Ask neighbors and nearby shops for information.", False),
            ("Request CCTV footage from nearby areas if available.", False),
            ("Keep your phone available for police updates.", False),
            ("Search calmly but quickly in nearby surroundings.", False),
            ("Do NOT delay reporting in hopes the child will return.", False),
            ("Do NOT panic in a way that delays action.", False),
        ],
    },
    (6, 4): {
        "title": "Elderly Care Services",
        "contacts": ["1122  –  Emergency Rescue", "Family Doctor / Caregiver"],
        "steps": [
            ("Check if the elderly person is conscious and responsive.", False),
            ("If unconscious or not breathing, call 1122 immediately.", False),
            ("If there is a fall or injury, do NOT move them unless necessary.", False),
            ("Keep them still and calm to avoid further injury.", False),
            ("Check for breathing, chest pain, dizziness, or stroke signs.", False),
            ("Call medical help for any serious symptoms.", False),
            ("Inform family members or caregiver immediately.", False),
            ("Keep essential medicines and medical history ready.", False),
            ("Provide comfort, warmth, and reassurance.", False),
            ("Do NOT ignore sudden confusion, weakness, or speech difficulty.", False),
            ("Do NOT give medication without medical advice.", False),
        ],
    },
    (7, 1): {
        "title": "Animal Cruelty & Rescue",
        "contacts": ["1122  –  Emergency Rescue", "Animal Rescue / Local Authority"],
        "steps": [
            ("Keep a safe distance from the injured or aggressive animal.", False),
            ("Do NOT attempt to handle or capture the animal yourself.", False),
            ("Call 1122 or local animal rescue services immediately.", False),
            ("Report exact location and condition of the animal.", False),
            ("Keep children and crowds away from the area.", False),
            ("Avoid provoking or stressing the animal further.", False),
            ("If a bite occurs, wash wound with soap and water immediately.", False),
            ("Seek medical attention as soon as possible.", False),
            ("If safe, provide water or shelter until help arrives.", False),
            ("Do NOT hit, chase, or corner the animal.", False),
            ("Do NOT ignore bites or injuries.", False),
        ],
    },
    (7, 2): {
        "title": "Dead Body Transport / Mortuary Services",
        "contacts": ["1122  –  Emergency Rescue", "15  –  Police (if required)"],
        "steps": [
            ("Check for any signs of breathing or response first.", False),
            ("Call 1122 immediately if death is sudden or medical emergency is unclear.", False),
            ("If death is suspicious, violent, or accidental, inform Police 15.", False),
            ("Do NOT move the body until authorities arrive in such cases.", False),
            ("Contact hospital, ambulance, or mortuary services for transport.", False),
            ("Keep identification documents and basic information ready.", False),
            ("Inform close family members or legal guardians immediately.", False),
            ("Follow hospital or legal procedures for certification.", False),
            ("Maintain dignity and respect for the deceased at all times.", False),
            ("Do NOT disturb the scene if it may be part of an investigation.", False),
            ("Do NOT attempt transport without official clearance in legal cases.", False),
        ],
    },
    (8, 1): {
        "title": "Major Water Leakage",
        "contacts": ["Local WASA / Water Authority"],
        "steps": [
            ("Turn off the main water supply immediately if accessible.", False),
            ("Switch off electricity in affected area if it is safe.", False),
            ("Move electrical appliances and valuables away from water.", False),
            ("Avoid walking through flooded or slippery areas.", False),
            ("Report the issue to the local water authority (WASA).", False),
            ("Give exact location and severity of the leak.", False),
            ("Use buckets or temporary barriers to reduce water spread if possible.", False),
            ("Keep children and elderly away from the affected area.", False),
            ("Do NOT touch electrical switches with wet hands.", False),
            ("Do NOT ignore water near electrical wiring or sockets.", False),
        ],
    },
    (8, 2): {
        "title": "Sewerage Overflow / Blockage",
        "contacts": ["Local Municipal Authority / WASA"],
        "steps": [
            ("Avoid contact with contaminated water or waste.", False),
            ("Keep children and elderly away from the area.", False),
            ("Report the issue to local municipal authority or WASA.", False),
            ("Provide exact location and severity of overflow.", False),
            ("Wear boots or protective gloves if you must pass nearby.", False),
            ("Wash hands thoroughly if exposed.", False),
            ("Avoid walking through stagnant or overflowing sewage water.", False),
            ("Keep doors and drains in surrounding areas closed if possible.", False),
            ("Do NOT touch contaminated surfaces with bare hands.", False),
            ("Do NOT ignore foul smell or repeated overflow issues.", False),
        ],
    },
    (8, 3): {
        "title": "Total Power Grid Failure",
        "contacts": ["118  –  WAPDA / Electricity Board"],
        "steps": [
            ("Stay calm and use alternative light sources like flashlights.", False),
            ("Turn off and unplug sensitive electrical appliances.", False),
            ("Avoid using elevators during power outage.", False),
            ("Check if neighbors are also affected to confirm outage scale.", False),
            ("Keep refrigerator and freezer closed to preserve food.", False),
            ("Use battery-powered devices for updates if available.", False),
            ("Check on elderly, children, and people using medical devices.", False),
            ("Avoid using candles near flammable materials.", False),
            ("Do NOT use generators indoors or in closed spaces.", False),
            ("Report outage to 118 or local electricity provider if needed.", False),
        ],
    },
    (8, 4): {
        "title": "Gas Supply Emergency",
        "contacts": ["SSGC / SNGPL  –  Gas Company", "16 / 1122  –  Fire Brigade"],
        "steps": [
            ("Do NOT switch on or off any electrical switches or appliances.", False),
            ("Do NOT use matches, lighters, candles, or any open flame.", False),
            ("Open doors and windows slowly to ventilate the area.", False),
            ("Turn off the main gas valve if it is safe to do so.", False),
            ("Evacuate the area immediately and move to a safe distance.", False),
            ("Warn others nearby calmly to leave the area.", False),
            ("Call gas company or emergency services from outside the area.", False),
            ("Do NOT use mobile phones inside the suspected leak area.", False),
            ("Do NOT create sparks (plugs, chargers, switches, motors).", False),
            ("Stay outside until authorities confirm it is safe.", False),
        ],
    },
}

# =====================
# COLORS & FONTS
# =====================
BG       = "#0f0f10"
SURFACE  = "#1a1a1e"
SURFACE2 = "#222228"
RED      = "#e8150f"
RED_DIM  = "#7a0a07"
TEXT     = "#f0ede8"
MUTED    = "#7a7870"
GREEN    = "#22c55e"
BORDER   = "#2a2a30"
GOLD     = "#f5c842"

# =====================
# APP
# =====================
class RapidReachApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RapidReach – Emergency Assistance System")
        self.geometry("900x720")
        self.minsize(700, 580)
        self.configure(bg=BG)
        self.resizable(True, True)

        self.current_cat = None

        self._build_header()
        self._build_content()
        self._build_footer()

        self.show_categories()

    # ── Header ──────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=SURFACE, pady=0)
        hdr.pack(fill="x")

        # ── Logo + RapidReach title on left ──
        top_row = tk.Frame(hdr, bg=SURFACE, pady=10, padx=20)
        top_row.pack(fill="x")

        # Logo box
        logo_box = tk.Frame(top_row, bg=RED, width=50, height=50)
        logo_box.pack(side="left")
        logo_box.pack_propagate(False)
        tk.Label(logo_box, text="RR", bg=RED, fg=TEXT,
                 font=("Courier", 17, "bold")).place(relx=0.5, rely=0.5, anchor="center")

        # Title + names stacked vertically
        title_frame = tk.Frame(top_row, bg=SURFACE)
        title_frame.pack(side="left", padx=(12, 0))

        # Big heading: RapidReach
        tk.Label(title_frame, text="RapidReach",
                 bg=SURFACE, fg=TEXT,
                 font=("Courier", 20, "bold")).pack(anchor="w")

        # Names below
        tk.Label(title_frame,
                 text="Warda Khan   ·   Nabeeha Ahmad",
                 bg=SURFACE, fg=GOLD,
                 font=("Courier", 11, "bold")).pack(anchor="w", pady=(2, 0))

        # Department
        tk.Label(title_frame,
                 text="Department of Physics and Applied Mathematics",
                 bg=SURFACE, fg=TEXT,
                 font=("Courier", 9)).pack(anchor="w")

        # University
        tk.Label(title_frame,
                 text="Pakistan Institute of Engineering and Applied Sciences  (PIEAS)",
                 bg=SURFACE, fg=MUTED,
                 font=("Courier", 8)).pack(anchor="w")

        # ── Thin red accent line at bottom of header ──
        tk.Frame(hdr, bg=RED, height=2).pack(fill="x")

    # ── Scrollable content area ──────────────────────────
    def _build_content(self):
        wrapper = tk.Frame(self, bg=BG)
        wrapper.pack(fill="both", expand=True, padx=16, pady=(12, 0))

        self.canvas = tk.Canvas(wrapper, bg=BG, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        sb = tk.Scrollbar(wrapper, orient="vertical", command=self.canvas.yview)
        sb.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=sb.set)

        self.inner = tk.Frame(self.canvas, bg=BG)
        self._win_id = self.canvas.create_window((0, 0), window=self.inner, anchor="nw")

        self.inner.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(
            self._win_id, width=e.width))
        self.canvas.bind_all("<MouseWheel>",
            lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

    # ── Footer ───────────────────────────────────────────
    def _build_footer(self):
        ft = tk.Frame(self, bg=SURFACE, pady=6)
        ft.pack(fill="x", side="bottom")
        tk.Label(ft, text="⚠  In a life-threatening emergency always call 1122 first",
                 bg=SURFACE, fg=RED, font=("Courier", 9, "bold")).pack()

    # ── Clear inner frame ────────────────────────────────
    def _clear(self):
        for w in self.inner.winfo_children():
            w.destroy()

    # ── Bind click to all children of a widget ──────────
    def _bind_click(self, widget, callback):
        widget.bind("<Button-1>", lambda e: callback())
        widget.configure(cursor="hand2")
        for child in widget.winfo_children():
            self._bind_click(child, callback)

    # ══════════════════════════════════════════════════════
    # SCREEN 1 – Categories (2-column grid)
    # ══════════════════════════════════════════════════════
    def show_categories(self):
        self._clear()
        self.current_cat = None

        # ── Big heading ──────────────────────────────────
        heading_frame = tk.Frame(self.inner, bg=BG)
        heading_frame.pack(fill="x", pady=(12, 6), padx=12)

        tk.Frame(heading_frame, bg=RED, height=3).pack(fill="x")

        tk.Label(heading_frame,
                 text="Emergency Categories",
                 bg=BG, fg=TEXT,
                 font=("Courier", 22, "bold")).pack(anchor="w", pady=(8, 2))

        tk.Label(heading_frame,
                 text="Choose a category below to view emergency types and response procedures",
                 bg=BG, fg=MUTED,
                 font=("Courier", 9)).pack(anchor="w")

        tk.Frame(heading_frame, bg=BORDER, height=1).pack(fill="x", pady=(8, 0))

        # ── 2-column grid ───────────────────────────────
        grid_frame = tk.Frame(self.inner, bg=BG)
        grid_frame.pack(fill="both", expand=True, padx=12, pady=10)

        grid_frame.columnconfigure(0, weight=1, uniform="col")
        grid_frame.columnconfigure(1, weight=1, uniform="col")

        for idx, (cat_id, label) in enumerate(CATEGORIES):
            row = idx // 2
            col = idx % 2
            grid_frame.rowconfigure(row, weight=1)

            # Card — entire card is clickable
            card = tk.Frame(grid_frame, bg=SURFACE2,
                            highlightbackground=BORDER, highlightthickness=1)
            card.grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

            # Number badge
            badge = tk.Frame(card, bg=RED, width=38, height=38)
            badge.pack(side="left", padx=(10, 8), pady=12)
            badge.pack_propagate(False)
            tk.Label(badge, text=str(cat_id), bg=RED, fg=TEXT,
                     font=("Courier", 14, "bold")).place(relx=0.5, rely=0.5, anchor="center")

            # Label
            txt_frame = tk.Frame(card, bg=SURFACE2)
            txt_frame.pack(side="left", fill="both", expand=True, pady=10)

            tk.Label(txt_frame, text=label,
                     bg=SURFACE2, fg=TEXT,
                     font=("Courier", 10, "bold"),
                     wraplength=260, justify="left").pack(anchor="w")

            # Hover highlight + click on entire card
            def _enter(e, c=card): c.configure(bg=SURFACE, highlightbackground=RED)
            def _leave(e, c=card): c.configure(bg=SURFACE2, highlightbackground=BORDER)

            callback = lambda cid=cat_id: self.show_subcategories(cid)
            self._bind_click(card, callback)

            for w in [card, txt_frame, badge]:
                w.bind("<Enter>", _enter)
                w.bind("<Leave>", _leave)

    # ══════════════════════════════════════════════════════
    # SCREEN 2 – Sub-categories
    # ══════════════════════════════════════════════════════
    def show_subcategories(self, cat_id):
        self._clear()
        self.current_cat = cat_id
        cat_label = next(l for cid, l in CATEGORIES if cid == cat_id)

        tk.Button(self.inner, text="← Back to Categories",
                  bg=SURFACE2, fg=TEXT, font=("Courier", 9),
                  relief="flat", cursor="hand2", padx=10, pady=5,
                  activebackground=SURFACE, activeforeground=TEXT,
                  command=self.show_categories).pack(anchor="w", padx=10, pady=(10, 4))

        tk.Label(self.inner, text=cat_label, bg=BG, fg=RED,
                 font=("Courier", 15, "bold"),
                 wraplength=700, justify="left").pack(anchor="w", padx=10, pady=(0, 2))
        tk.Frame(self.inner, bg=BORDER, height=1).pack(fill="x", padx=10, pady=(0, 8))

        for idx, sub in enumerate(SUBS[cat_id], start=1):
            row = tk.Frame(self.inner, bg=SURFACE2,
                           highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", padx=10, pady=4)

            tk.Label(row, text=f"{idx:02d}", bg=RED, fg=TEXT,
                     font=("Courier", 11, "bold"), width=4, pady=12).pack(side="left")

            tk.Label(row, text=sub, bg=SURFACE2, fg=TEXT,
                     font=("Courier", 10), anchor="w").pack(
                     side="left", fill="x", expand=True, padx=10)

            # Hover highlight + click on entire row
            def _enter(e, r=row): r.configure(bg=SURFACE, highlightbackground=RED)
            def _leave(e, r=row): r.configure(bg=SURFACE2, highlightbackground=BORDER)

            callback = lambda cid=cat_id, si=idx: self.show_info(cid, si)
            self._bind_click(row, callback)

            row.bind("<Enter>", _enter)
            row.bind("<Leave>", _leave)
            for child in row.winfo_children():
                child.bind("<Enter>", _enter)
                child.bind("<Leave>", _leave)

    # ══════════════════════════════════════════════════════
    # SCREEN 3 – Info / Steps
    # ══════════════════════════════════════════════════════
    def show_info(self, cat_id, sub_idx):
        self._clear()
        key  = (cat_id, sub_idx)
        data = INFO.get(key)

        cat_label = next(l for cid, l in CATEGORIES if cid == cat_id)

        tk.Button(self.inner,
                  text=f"← Back to {cat_label.split('  ')[-1]}",
                  bg=SURFACE2, fg=TEXT, font=("Courier", 9),
                  relief="flat", cursor="hand2", padx=10, pady=5,
                  activebackground=SURFACE, activeforeground=TEXT,
                  command=lambda: self.show_subcategories(cat_id)).pack(
                  anchor="w", padx=10, pady=(10, 4))

        if not data:
            tk.Label(self.inner, text="No information available.",
                     bg=BG, fg=MUTED, font=("Courier", 11)).pack(padx=10, pady=20)
            return

        tk.Label(self.inner, text=data["title"], bg=BG, fg=RED,
                 font=("Courier", 15, "bold"),
                 wraplength=700, justify="left").pack(anchor="w", padx=10, pady=(0, 4))

        # Contacts box
        cf = tk.Frame(self.inner, bg=SURFACE2,
                      highlightbackground=RED, highlightthickness=1)
        cf.pack(fill="x", padx=10, pady=(0, 10))
        tk.Label(cf, text="📞  Emergency Contacts",
                 bg=SURFACE2, fg=RED,
                 font=("Courier", 10, "bold")).pack(anchor="w", padx=10, pady=(6, 2))
        for c in data["contacts"]:
            tk.Label(cf, text=f"   {c}", bg=SURFACE2, fg=GREEN,
                     font=("Courier", 10)).pack(anchor="w", padx=10)
        tk.Label(cf, text="", bg=SURFACE2).pack()

        # Steps — all uniform, no warning styling
        tk.Label(self.inner, text="Response Steps", bg=BG, fg=TEXT,
                 font=("Courier", 11, "bold")).pack(anchor="w", padx=10, pady=(0, 4))

        for i, (step, _) in enumerate(data["steps"], start=1):
            sf = tk.Frame(self.inner, bg=SURFACE2,
                          highlightbackground=BORDER, highlightthickness=1)
            sf.pack(fill="x", padx=10, pady=2)

            tk.Label(sf, text=f"{i:02d}. {step}",
                     bg=SURFACE2, fg=TEXT,
                     font=("Courier", 10),
                     wraplength=680, justify="left", anchor="w").pack(
                     anchor="w", padx=10, pady=5)


if __name__ == "__main__":
    app = RapidReachApp()
    app.mainloop()