from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}
    try:
        file=open(fileName,'r')
    except FileNotFoundError:
        print(f"The file could not be found")
        exit()
    try:
        patients_list=file.readlines()
    except:
        print("An unexpected error occurred while reading the file")
    patient_detail = []
    for i in range(0,len(patients_list)):
        line= patients_list[i].strip().split(',')
        #if fields are not 8
        if len(line)!=8: 
            print(f"Invalid number of fields {len(line)} in line:{i+1}")
        patient=[]
        patientId=int(line[0])
        date=line[1]        # date
        temp=float(line[2]) # temperature
        hr=int(line[3])     # heart rate
        rr=int(line[4])     # respiratory rate
        sbp=int(line[5])    # systolic blood pressure
        dbp=int(line[6])    # diastolic blood pressure
        spo2=int(line[7])   # oxygen saturation value
        try:
            patient_detail=[date,temp,hr,rr,sbp,dbp,spo2]
        except TypeError:
            print(f"Invalid data type in line:{i+1}")
        # if temperatue not in range of 35 to 42
        if temp<35 and temp>42:
            print(f"Invalid temperature value {temp} in line:{i+1}")

        # if heart rate is not in range of 30 to 180
        if hr<30 and hr>180:
            print(f"Invalid heart rate value {hr} in line: {i+1}")

        # if respiratory rate is not in range 5 to 40
        if rr<5 and rr>40:
            print(f"Invalid respiratory rate value {rr} in line: {i+1}")

        # if the systolic blood pressure is not in range 70 to 200
        if sbp<70 and sbp>200:
            print(f"Invalid systolic blood pressure value {sbp} in line:{i+1}")

        #if the diastolic blood pressure is not in range 40 to 120
        if dbp<40 and dbp>120: 
            print(f"Invalid diastolic blood pressure value {dbp} in line:{i + 1}")

        # if the oxygen saturation is not in range 70 to 100
        if spo2<70 and spo2>100:
            print(f"Invalid oxygen saturation value {spo2} in line:{i+1}")
        if patientId in patients:
            patients[patientId].append(patient_detail)
        else:
            patients[patientId]=[patient_detail]

    return patients

def displayPatientData(patients, patientId):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    # Check if the patientId is 0 (display data for all patients)
    if patientId == 0:
        # Check Every individual element in the patient
        for key,value in patients.items():
            print(f"Patient ID:{key}")
            for details in value:
                print(f" Visit Date:{details[0]}")
                print(f"   Temperature:{details[1]}")
                print(f"   Heart Rate:{details[2]} C")
                print(f"   Respirotary Rate:{details[3]} bpm")
                print(f"   Systolic Blood Pressure:{details[4]} bpm")
                print(f"   Diastolic Blood Pressure:{details[5]} mmHg")
                print(f"   Oxygen Saturation:{details[6]} mmHg")
                print("\n")

    else:
        # Display data for the specific patientId
        if patientId in patients:
            value=patients[patientId]
            for details in value:
                print(f" Visit Date:{details[0]}")
                print(f"   Temperature:{details[1]}")
                print(f"   Heart Rate:{details[2]} C")
                print(f"   Respirotary Rate:{details[3]} bpm")
                print(f"   Systolic Blood Pressure:{details[4]} bpm")
                print(f"   Diastolic Blood Pressure:{details[5]} mmHg")
                print(f"   Oxygen Saturation:{details[6]} mmHg")
                print("\n")
        else:
            print(f"Patient with ID {patientId} not found.")
   


def displayStats(patients, patientId):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """
    patientId=int(patientId)
    try:
        if not isinstance(patients, dict):
            print("Invalid patient data format.")
        
        # Check if the patientId is 0 (display stats for all patients)
        if patientId == 0:
            all_temperatures = []
            all_heart_rates = []
            all_respiratory_rates = []
            all_systolic_bps = []
            all_diastolic_bps = []
            all_oxygen_saturations = []

            #Add all the indiviual elements in their repective lists
            for key,value in patients.items():
                for visit in value:
                    all_temperatures.append(visit[1])
                    all_heart_rates.append(visit[2])
                    all_respiratory_rates.append(visit[3])
                    all_systolic_bps.append(visit[4])
                    all_diastolic_bps.append(visit[5])
                    all_oxygen_saturations.append(visit[6])

            #Find the average
            total_visits = len(all_temperatures)
            average_temperature = sum(all_temperatures) / total_visits
            average_heart_rate = sum(all_heart_rates) / total_visits
            average_respiratory_rate = sum(all_respiratory_rates) / total_visits
            average_systolic_bp = sum(all_systolic_bps) / total_visits
            average_diastolic_bp = sum(all_diastolic_bps) / total_visits
            average_oxygen_saturation = sum(all_oxygen_saturations) / total_visits

            #Print the Average of Each vital Signs
            print("Average Vital Signs for All Patients:")
            print(f"Average Temperature: {average_temperature:.2f}°C")
            print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")
            print(f"Average Respiratory Rate: {average_respiratory_rate:.2f} bpm")
            print(f"Average Systolic Blood Pressure: {average_systolic_bp:.2f} mmHg")
            print(f"Average Diastolic Blood Pressure: {average_diastolic_bp:.2f} mmHg")
            print(f"Average Oxygen Saturation: {average_oxygen_saturation:.2f}%")

        else:

            # Display stats for the specific patientId
            if patientId in patients:
                patient_data = patients[patientId]
                total_visits = len(patient_data)
                if total_visits == 0:
                    print(f"No visits recorded for Patient ID {patientId}.")
                    return
                
                #Store the total for each vital Signs
                total_temperature = sum(visit[1] for visit in patient_data)
                total_heart_rate = sum(visit[2] for visit in patient_data)
                total_respiratory_rate = sum(visit[3] for visit in patient_data)
                total_systolic_bp = sum(visit[4] for visit in patient_data)
                total_diastolic_bp = sum(visit[5] for visit in patient_data)
                total_oxygen_saturation = sum(visit[6] for visit in patient_data)

                #Find the average for each vital signs
                average_temperature = total_temperature / total_visits
                average_heart_rate = total_heart_rate / total_visits
                average_respiratory_rate = total_respiratory_rate / total_visits
                average_systolic_bp = total_systolic_bp / total_visits
                average_diastolic_bp = total_diastolic_bp / total_visits
                average_oxygen_saturation = total_oxygen_saturation / total_visits

                #Print the Average Vital Signs for A specfic pattient
                print(f"Average Vital Signs for Patient ID {patientId}:")
                print(f"Average Temperature: {average_temperature:.2f}°C")
                print(f"Average Heart Rate: {average_heart_rate:.2f} bpm")
                print(f"Average Respiratory Rate: {average_respiratory_rate:.2f} bpm")
                print(f"Average Systolic Blood Pressure: {average_systolic_bp:.2f} mmHg")
                print(f"Average Diastolic Blood Pressure: {average_diastolic_bp:.2f} mmHg")
                print(f"Average Oxygen Saturation: {average_oxygen_saturation:.2f}%")
            else:
                print(f"Patient with ID {patientId} not found.")

        
    except ValueError as x:
        print(f"Error: {x}")
    except TypeError as y:
        print(f"Error: {y}")



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    file=open(fileName,'a')
    try:
        yyyy,mm,dd=date.split('-')
        year=int(yyyy)
        month=int(mm)
        day=int(dd)
        count=1
        #to check for valid date
        if (day<1 or day>31) or (month<1 or month>12) or year<1900:
            print("Invalid date. Please enter a valid date.")
            count=0
        #to check temperature
        if temp<35.0 or temp>42.0:
            print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius")
            count=0
        #to check heart rate
        if hr<30 or hr>180:
            print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm")
            count=0
        #to check respiratory rate
        if rr<5 or rr>40:
            print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm")
            count=0
        #to check systolic blood pressure
        if sbp<70 or sbp>200:
            print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg")
            count=0
        #to check diastolic blood pressure
        if dbp<40 or dbp>120:
            print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg")
            count=0
        #to check oxygen saturation
        if spo2<70 or spo2>100:
            print("Invalid oxygen saturation.Please enter an oxygen saturation between 70 and 100%")
            count=0
        if count:    
            #adding the data
            try:
                patient_detail=str(patientId)+','+str(date)+','+str(temp)+','+str(hr)+','+str(rr)+','+str(sbp)+','+str(dbp)+','+str(spo2)
                file.write('\n'+patient_detail)
            except:
                print("An unexpected error occurred while adding new data")
        else:
            return    
    except:
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd' ")



def findVisitsByDate(patients, year, month):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    
    #Check patients is a dictonary or not
    if not isinstance(patients, dict):
        print("Invalid patient data format.")
        return visits
    
    #Extract the date and year from the patient dictionary
    for key, value in patients.items():
        for visit in value:
            visit_date = visit[0]

            # Splitting the date into year, month, and day components
            try:
                visit_date= visit_date.split('-')
                visit_year = int(visit_date[0])
                visit_month = int(visit_date[1])
            except ValueError:
                # Skip visits with invalid date format
                continue
            # Check if the visit matches the filter criteria
            if (year is None or visit_year == year) and (month is None or visit_month == month):
                visits.append((key, visit))

    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []
    #Search from the patient dictionary
    for key, value in patients.items():
        needs_followup = 0

        for visit in value:
                heart_rate =visit[2] 
                systolic_bp = visit[4]
                diastolic_bp = visit[5]
                spo2 = visit[6]

                #If condition Satisfy append the key(patiend id) in followip_patiends
                if heart_rate > 100 or heart_rate < 60 or systolic_bp > 140 or diastolic_bp > 90 or spo2 < 90:
                    needs_followup = 1
                    break  # No need to check other visits for this patient

        if needs_followup:
            followup_patients.append(key)

    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    if patientId in patients:
            patients.pop(patientId)
            
            # Update the file with the modified patient data
            file=open(filename,'w')
            for key, value in patients.items():
                for visit in value:
                    visit_data = ','.join(str(field) for field in visit)
                    file.write(f"{key},{visit_data}\n")
            
            print(f"Data for patient {patientId} has been deleted.")
    else:
            print(f"No data found for patient with ID {patientId}.")




###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
            displayPatientData(patients,0)
        elif choice == '2':
            patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'PROJECT PYTHON\patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            patients = readPatientsFromFile('PROJECT PYTHON/patients.txt')
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "PROJECT PYTHON/patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()