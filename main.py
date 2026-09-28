from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import sqlite3
from datetime import date
from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDButton, MDButtonText
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, MDListItem,  MDListItemHeadlineText, MDListItemSupportingText
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.popup import Popup
#from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.card import MDCard

KV="""
<MainScreen>:
    MDBoxLayout:  
        orientation: 'vertical'
        padding: 10
        spacing: 5
        md_bg_color: "#e7e4c0"  

        MDLabel:
            id: total
            text: 'Total'
            halign: "center"
            font_size: "20sp"
            bold: True
            size_hint_y: 0.55
            text_color: 1,0,.5,1

        ScrollView:
            MDBoxLayout: #balance layout
                id: box
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                md_bg_color:  "#e7e4c0"
                padding: 10
                spacing: 5
                                      
        MDBoxLayout:
            size_hint_y: None
            spacing: "0dp"
            MDButton:
                style: "filled"
                on_release: root.manager.current = 'new_ipo'
                MDButtonText:
                    text: 'NEW IPO'
                    bold:True
            MDButton:
                style: "filled"
                on_release: root.manager.current = 'allot'
                MDButtonText:
                    text: 'ALLOTMENT' 
                    bold:True
            MDButton:
                style: "filled"
                on_release: root.manager.current = 'manual_update'
                MDButtonText:
                    text: 'MANUAL UPDATE' 
                    bold:True
            
<NewIPOScreen>:
    name: 'new_ipo'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 5
        md_bg_color: "#e7e4c0" 
        spacing: 5
        
        TextInput:
            id: ipo_name
            hint_text: 'ENTER IPO Name'
            size_hint_y: None
            height: "40dp"
            
        TextInput:
            id: ipo_amt
            hint_text: 'IPO Amount'
            input_filter: 'int'
            size_hint_y: None
            height: "40dp"

        MDLabel:
            text: "Select IPO Bidders"
            halign: "center"
            size_hint_y: None
            height: "30dp"
            text_color: 1,0,.5,1
            bold: True

        ScrollView:
            MDBoxLayout:
                id: table_box
                orientation: 'vertical'
                height: self.minimum_height
                spacing: 5
                padding: 5
                md_bg_color:  "#e7e4c0"
        
        MDBoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: 10
            padding: [0,5,0,0]
            
            MDButton:
                style: "filled"
                on_press: root.confirm_ipo()
                MDButtonText:
                    text: 'SUBMIT RECORD'
                    bold:True

            MDButton:
                style: "filled"
                on_press: root.manager.current = 'main'
                MDButtonText:
                    text: 'BACK'
                    bold:True
        

<ManualUpdateScreen>:
    name: 'manual_update'

    MDBoxLayout:
        orientation: "vertical"
        padding: "15dp"
        spacing: "10dp"
        md_bg_color: "#e7e4c0"

        MDLabel:
            text: "MANUAL DATABASE UPDATE"
            halign: "center"
            font_style: "Title"
            bold: True
            size_hint_y: None
            height: "45dp"
            text_color: 0, 0, 1, 1

        Spinner:
            id: holder
            text: "SELECT HOLDER"
            values: ["Parkash", "Nitesh", "Sonam", "Smayra", "Siya", "Sandeep"]
            size_hint_y: None
            height: "50dp"
            background_color: 0.8, 0.8, 0.8, 1

        TextInput:
            id: bank_bal
            hint_text: "ENTER BANK BALANCE"
            input_filter: "int"
            multiline: False
            size_hint_y: None
            height: "50dp"

        TextInput:
            id: demat_bal
            hint_text: "ENTER DEMAT BALANCE"
            input_filter: "int"
            multiline: False
            size_hint_y: None
            height: "40dp"

        TextInput:
            id: demat_hold
            hint_text: "ENTER DEMAT HOLD"
            input_filter: "int"
            multiline: False
            size_hint_y: None
            height: "40dp"

        TextInput:
            id: share_amt
            hint_text: "ENTER SHARE AMOUNT"
            input_filter: "int"
            multiline: False
            size_hint_y: None
            height: "40dp"

        Widget:

        MDBoxLayout:
            size_hint_y: None
            height: "55dp"
            spacing: "10dp"

            MDButton:
                style: "filled"
                on_release: root.confirm_update()
                MDButtonText:
                    text: "UPDATE DATABASE"
                    bold:True

            MDButton:
                style: "filled"
                on_release: root.manager.current = "main"
                MDButtonText:
                    text: "BACK"
                    bold:True


        
<AllotScreen>:
    name: 'allot'
    MDBoxLayout:
        orientation: "vertical"
        padding: "10dp"
        spacing: "10dp"
        md_bg_color: "#e7e4c0" 

        MDLabel:
            text: "IPO ALLOTMENT"
            halign: "center"
            font_style: "Title"
            role: "large"
            size_hint_y: None
            height: "30dp"
            text_color: 0,0,1,1
            bold: True

        # IPO RADIO BUTTON AREA
        MDBoxLayout:
            id: ipo_box
            orientation: "vertical"
            size_hint_y: .05
            height: self.minimum_height
            spacing: "5dp"
            md_bg_color: "#e7e4c0" 
            padding: 5
            radius: [5,5,5,5]
            

        # HOLDER TABLE AREA
        ScrollView:
            MDBoxLayout:
                id: table_box
                orientation: "vertical"
                #size_hint_y: None
                height: self.minimum_height
                spacing: 5

        MDBoxLayout:
            size_hint_y: None
            height: "50dp"
            spacing: "10dp"
            

            MDButton:
                style: "filled"
                on_press: root.confirm_allotment()
                MDButtonText:
                    text: "SUBMIT ALLOTMENT"
                    bold:True

            MDButton:
                style: "filled"
                on_press: root.manager.current = "main"
                MDButtonText:
                    text: "BACK"
                    bold:True
"""


DB_NAME = "IPO_Records.db"
HOLDERS = ['Parkash','Nitesh','Sonam','Smayra','Siya','Sandeep']
def get_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    for h in HOLDERS:
        cur.execute(f"CREATE TABLE IF NOT EXISTS {h} (SR_No INTEGER PRIMARY KEY AUTOINCREMENT, IPO_Date TEXT, IPO_Name TEXT, IPO_Amount INTEGER, Bank_Bal INTEGER DEFAULT 0, Demat_Bal INTEGER DEFAULT 0, Demat_Hold INTEGER DEFAULT 0, Share_Amount INTEGER DEFAULT 0, Allotment_Status TEXT DEFAULT Pending)")
        cur.execute(f"SELECT COUNT(*) FROM {h}")
        if cur.fetchone()[0] == 0:
            cur.execute(f"INSERT INTO {h} (IPO_Date, IPO_Name, IPO_Amount, Bank_Bal) VALUES (?,?,?,?)", (str(date.today()), "Opening", 0, 0))
    conn.commit()
    return conn
class MainScreen(MDScreen):
    def refresh_data(self):
        self.ids.box.clear_widgets()
        conn = get_db()
        cur = conn.cursor()
        total_bal = 0
        total_bank =0
        total_hold = 0
        total_share =0
        total_demat=0

        for h in HOLDERS:
            cur.execute(f"SELECT Bank_Bal, Demat_Hold, Share_Amount,Demat_Bal FROM {h} WHERE SR_No=(SELECT MAX(SR_No) FROM {h})")
            r = cur.fetchone()
            if r:
                total_bal += (r[0] or 0) + (r[1] or 0) + (r[2] or 0)
                total_bank += (r[0] or 0)
                total_hold += (r[1] or 0)
                total_share += (r[2] or 0)
                total_demat += (r[3] or 0)


                bal_box = MDBoxLayout(
                    orientation='vertical',
                    size_hint_y=None,
                    height="60dp",
                    md_bg_color="#e2b7c1" ,
                    padding=5,
                    spacing=5,
                    radius=[8,8,8,8]
                )

                # Holder ka naam - bold me
                bal_box.add_widget(MDLabel(
                    text=f"{h}",
                    bold=True,
                    font_size="10sp",
                    theme_text_color="Custom",
                    text_color="#323212", # Sunehra naam
                    #size_hint_y=None,
                    height="0dp"
                ))

                # Balance details - alag color me
                bal_box.add_widget(MDLabel(
                    text=f"Bank: Rs.{r[0]} | Hold: Rs.{r[1]} | Share: Rs.{r[2]} | Demat: Rs.{r[3]}",
                    font_size="10sp",
                    theme_text_color="Custom",
                    text_color="#2C0303", 
                    #size_hint_y=None,
                    height="0dp"
                ))

                self.ids.box.add_widget(bal_box)

        self.ids.total.text = f"Total Family Balance: Rs. {total_bal} \nTotal in Bank : Rs. {total_bank} \nTotal in Hold : Rs. {total_hold} \nTotal in Share: Rs. {total_share}\nTotal in Demat: Rs. {total_demat}"
        conn.close()

    def on_enter(self): self.refresh_data()
    
        
class ManualUpdateScreen(MDScreen):

    def confirm_update(self):

        holder = self.ids.holder.text

        if holder == "SELECT HOLDER":
            return

        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"
        )

        message = MDLabel(
            text=f"Update balance for {holder}?",
            bold=True
        )

        button_box = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=50,
            md_bg_color="#DADCC3"
        )

        yes_btn = MDButton(
            MDButtonText(text="YES")
        )

        no_btn = MDButton(
            MDButtonText(text="CANCEL")
        )

        button_box.add_widget(yes_btn)
        button_box.add_widget(no_btn)

        content.add_widget(message)
        content.add_widget(button_box)

        self.popup = Popup(
            title="Confirm Manual Update",
            content=content,
            size_hint=(0.5, 0.35),
            auto_dismiss=False
        )

        no_btn.bind(
            on_release=lambda x: self.popup.dismiss()
        )

        yes_btn.bind(
            on_release=lambda x: self.update_database()
        )

        self.popup.open()


    def update_database(self):

        self.popup.dismiss()

        holder = self.ids.holder.text

        if holder == "SELECT HOLDER":
            return

        # Empty textbox ko 0 maana jayega
        bank_bal = self.ids.bank_bal.text.strip()
        demat_bal = self.ids.demat_bal.text.strip()
        demat_hold = self.ids.demat_hold.text.strip()
        share_amt = self.ids.share_amt.text.strip()

        bank_bal = int(bank_bal) if bank_bal else 0
        demat_bal = int(demat_bal) if demat_bal else 0
        demat_hold = int(demat_hold) if demat_hold else 0
        share_amt = int(share_amt) if share_amt else 0

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        # Latest record ka SR_No
        cur.execute(
            f"""
            SELECT MAX(SR_No)
            FROM {holder}
            """
        )

        result = cur.fetchone()

        if not result or result[0] is None:
            conn.close()
            return

        latest_sr = result[0]

        # Latest record update
        cur.execute(
            f"""
            UPDATE {holder}
            SET
                Bank_Bal = ?,
                Demat_Bal = ?,
                Demat_Hold = ?,
                Share_Amount = ?
            WHERE SR_No = ?
            """,
            (
                bank_bal,
                demat_bal,
                demat_hold,
                share_amt,
                latest_sr
            )
        )

        conn.commit()
        conn.close()

        # TextBox clear
        self.ids.bank_bal.text = ""
        self.ids.demat_bal.text = ""
        self.ids.demat_hold.text = ""
        self.ids.share_amt.text = ""

        self.ids.holder.text = "SELECT HOLDER"

        self.success_msg()


    def success_msg(self):

        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"
        )

        message = MDLabel(
            text="Database Updated Successfully!",
            bold=True
        )

        back_btn = MDButton(
            MDButtonText(text="BACK")
        )

        content.add_widget(message)
        content.add_widget(back_btn)

        self.success_popup = Popup(
            title="Update Successful",
            content=content,
            size_hint=(0.5, 0.35),
            auto_dismiss=False
        )

        back_btn.bind(
            on_release=self.close_success
        )

        self.success_popup.open()


    def close_success(self, *args):

        self.success_popup.dismiss()
        self.manager.current = "main"



class NewIPOScreen(MDScreen):

    def on_enter(self):
        self.show_table()

    def show_table(self):

        HOLDERSS = [("Parkash",),("Nitesh",),("Sonam",),("Smayra",),("Siya",),("Sandeep",)]

        self.table = MDDataTable(
            size_hint=(0.99, 0.99),
            pos_hint={"center_x": 0.5, "center_y": 0.5},

            use_pagination=True,
            rows_num=6,

            check=True,

            column_data=[
                ("All Select", dp(200))
            ],

            row_data=HOLDERSS
        )

        self.ids.table_box.clear_widgets()
        self.ids.table_box.add_widget(self.table)

    def confirm_ipo(self):
    
        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"
            
        )

        message = MDLabel(
            text="Are you sure you want to submit this ipo record?",
            bold=True
        )

        button_box = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=50,
            md_bg_color="#DADCC3"
        )

        yes_btn = MDButton(
            MDButtonText(text="YES")
        )
        no_btn = MDButton(
            MDButtonText(text="CANCEL")
        )
        

        
        button_box.add_widget(yes_btn)
        button_box.add_widget(no_btn)

        content.add_widget(message)
        content.add_widget(button_box)

        self.popup = Popup(
            title="Confirm Submission",
            content=content,
            size_hint=(0.6, 0.35),
            auto_dismiss=False
        )

        no_btn.bind(
            on_release=lambda x: self.popup.dismiss()
        )

        yes_btn.bind(
            on_release=lambda x: self.submit_ipo()
        )

        
        self.popup.open()
    def submit_ipo(self):
        ipo_name = self.ids.ipo_name.text.strip()
        ipo_amt = self.ids.ipo_amt.text.strip()
        self.popup.dismiss()
        if not ipo_name:
            #print("IPO Name enter karo")
            return

        if not ipo_amt:
            #print("IPO Amount enter karo")
            return

        try:
            ipo_amt = int(ipo_amt)
        except ValueError:
            #print("Amount sirf number hona chahiye")
            return
        selected_rows = self.table.get_row_checks()

        if not selected_rows:
            #print("Koi holder select nahi hai")
            return

        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()

        for row in selected_rows:

            holder_name = row[0]
            if holder_name == "Smayra" or holder_name == "Siya":
                cur.execute(f""" SELECT Demat_Hold,Share_Amount FROM {holder_name} WHERE SR_No = (SELECT MAX(SR_No) FROM {holder_name} )""")
                hold = cur.fetchone()
                demat_hold = hold[0] or 0
                share_amt = hold[1] or 0
                new_demat_hold = demat_hold + ipo_amt
                cur.execute(f""" INSERT INTO {holder_name}(IPO_Date, IPO_Name, IPO_Amount,Demat_Hold,Share_Amount) VALUES (?, ?, ?,?,?)""",(str(date.today()),ipo_name,ipo_amt,new_demat_hold,share_amt))
                conn.commit()


                cur.execute(f""" SELECT Bank_Bal FROM Nitesh  WHERE SR_No = ( SELECT MAX(SR_No) FROM Nitesh)""")
                balance = cur.fetchone()
                bank_bal = balance[0] or 0
                new_bank_bal = bank_bal - ipo_amt
                cur.execute(f"""UPDATE Nitesh SET Bank_Bal=? WHERE SR_No = (SELECT MAX(SR_No) FROM Nitesh)""",(new_bank_bal,))
                


            else:
                cur.execute(f""" SELECT Bank_Bal, Demat_Hold,Share_Amount FROM {holder_name} WHERE SR_No = (SELECT MAX(SR_No) FROM {holder_name})""")
                balance = cur.fetchone()
                bank_bal = balance[0] or 0
                demat_hold = balance[1] or 0
                share_amt = balance[2] or 0
                new_bank_bal = bank_bal - ipo_amt
                new_demat_hold = demat_hold + ipo_amt
                cur.execute(f""" INSERT INTO {holder_name} (IPO_Date,IPO_Name,IPO_Amount,Bank_Bal,Demat_Hold,Share_Amount) VALUES (?, ?, ?,?,?,?) """,(str(date.today()),ipo_name,ipo_amt,new_bank_bal,new_demat_hold,share_amt ))

        conn.commit()
        conn.close()

        # Optional: fields clear
        self.ids.ipo_name.text = ""
        self.ids.ipo_amt.text = ""
        self.success_msg()
    
    
    
    def success_msg(self):
        
        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"
            
        )

        message = MDLabel(
            text="IPO Applied Successfully!",
            bold=True
        )

        button_box = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=50,
            md_bg_color="#DADCC3"
        )

        back_btn = MDButton(
            MDButtonText(text="BACK")
        )

        button_box.add_widget(back_btn)

        content.add_widget(message)
        content.add_widget(button_box)

        self.success_popup = Popup(
            title="IPO Applied Successfully",
            content=content,
            size_hint=(0.45, 0.35),
            auto_dismiss=False
        )

        back_btn.bind(on_release=self.back_to_main)

        self.success_popup.open()
    def back_to_main(self, *args):
        self.success_popup.dismiss()
        self.manager.current = "main"


class AllotScreen(MDScreen):

    def on_enter(self):
        self.ipo_seletion()

    def ipo_seletion(self):

        conn = get_db()
        cur = conn.cursor()

        check_pending_ipo = []

        for h in HOLDERS:

            cur.execute(f""" SELECT DISTINCT IPO_Name FROM {h} WHERE Allotment_Status = 'Pending' AND IPO_Name IS NOT NULL  AND IPO_Name != '' AND IPO_Name != 'Opening'""" )

            pending_ipos = cur.fetchall()

            for pend_ipo in pending_ipos:

                pending_ipo = pend_ipo[0]

                if pending_ipo not in check_pending_ipo:
                    check_pending_ipo.append(pending_ipo)

        conn.close()

        #print("AVAILABLE IPO =", check_pending_ipo)

        self.ids.ipo_box.clear_widgets()

        self.selected_ipo = None

        ipo_layout = MDBoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            padding=dp(5),
            size_hint_y=None,
            height=dp(50)
        )

        for ipo in check_pending_ipo:

            checkbox = MDCheckbox(
                group="ipo"
            )

            # IPO name checkbox ke saath attach
            checkbox.ipo_name = ipo

            # IMPORTANT
            checkbox.bind(
                active=self.ipo_selected
            )

            label = MDLabel(
                text=ipo,
                size_hint_x=None,
                width=dp(120)
            )

            ipo_layout.add_widget(checkbox)
            ipo_layout.add_widget(label)

        self.ids.ipo_box.add_widget(ipo_layout)


    # ---------------------------------
    # RADIO BUTTON SELECT FUNCTION
    # ---------------------------------

    def ipo_selected(self, checkbox, active):

        if active:
            self.selected_ipo = checkbox.ipo_name
            self.selected()


    # ---------------------------------
    # SUBMIT IPO NAME
    # ---------------------------------

    def selected(self):

        if not self.selected_ipo:

            #print("Pehle IPO select karo")

            return

        self.ipo = self.selected_ipo

        #print("FETCHING IPO =", ipo)

        conn = get_db()
        cur = conn.cursor()

        self.rows = []

        for h in HOLDERS:

            cur.execute(f"""SELECT IPO_Date, IPO_Name, IPO_Amount FROM {h} WHERE IPO_Name = ? AND Allotment_Status = 'Pending'  """, (self.ipo,) )

            result = cur.fetchone()

            if result:

                ipo_date, ipo_name, ipo_amount = result

                self.rows.append(
                    (
                        h,
                        str(ipo_date),
                        str(ipo_name),
                        str(ipo_amount)
                    )
                )

        conn.close()

        #print("FETCHED ROWS =", self.rows)

        if not self.rows:

            #print("Is IPO ka pending record nahi mila")

            self.ids.table_box.clear_widgets()

            return

        self.table = MDDataTable(

            size_hint=(0.99, 0.99),

            pos_hint={
                "center_x": 0.5,
                "center_y": 0.5
            },

            use_pagination=True,

            rows_num=6,

            check=True,

            column_data=[
                ("Holder", dp(35)),
                ("IPO Date", dp(35)),
                ("IPO Name", dp(35)),
                ("Amount", dp(35)),
            ],

            row_data=self.rows
        )

        self.ids.table_box.clear_widgets()

        self.ids.table_box.add_widget(self.table)





    def confirm_allotment(self):

        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"

        )

        message = MDLabel(
            text="Are you sure you want to submit this allotment?",
            bold=True
        )

        button_box = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=50,
            md_bg_color="#DADCC3"
        )

        yes_btn = MDButton(
            MDButtonText(text="YES")
        )
        no_btn = MDButton(
            MDButtonText(text="CANCEL")
        )
        

        
        button_box.add_widget(yes_btn)
        button_box.add_widget(no_btn)

        content.add_widget(message)
        content.add_widget(button_box)

        self.popup = Popup(
            title="Confirm Allotment",
            content=content,
            size_hint=(0.6, 0.35),
            auto_dismiss=False
        )

        no_btn.bind(
            on_release=lambda x: self.popup.dismiss()
        )

        yes_btn.bind(
            on_release=lambda x: self.submit_allotment()
        )

        self.popup.open()


    def submit_allotment(self):
        self.popup.dismiss()
        conn = get_db()
        cur = conn.cursor()
        bidders=self.rows # jinhone bid lgaayi h 
        bidders_name= set() # name jinhone bid lgayi thi 
        alloted = self.table.get_row_checks() # info jinko allot hua h
        alloted_name= set() #  name jinko allot hua h 
        for bidder in bidders:
            bidders_name.add(bidder[0])
        for row in alloted:
            holder_name = row[0]
            alloted_name.add(holder_name)
            cur.execute(f""" SELECT IPO_Amount FROM {holder_name} WHERE IPO_Name = ?""",(self.ipo,))
            amnt=cur.fetchone()
            ipo_amt = amnt[0] or 0
            cur.execute(f""" SELECT Demat_Hold ,Share_Amount FROM {holder_name} WHERE SR_No = (SELECT MAX(SR_No) FROM {holder_name} )""")
            hold = cur.fetchone()
            hold_amount = hold[0] or 0
            share_amount = hold[1] or 0
            hold_amount_aftr_allotment = hold_amount - ipo_amt
            share_amount_aftr_allotment = share_amount + ipo_amt
            cur.execute(f""" UPDATE {holder_name} SET  Allotment_Status = 'Yes' WHERE IPO_Name=? """,(self.ipo,))
            cur.execute(f""" UPDATE {holder_name} SET Demat_Hold=? ,Share_Amount=? WHERE SR_No = (SELECT MAX(SR_No) FROM {holder_name} )""",(hold_amount_aftr_allotment,share_amount_aftr_allotment))
            conn.commit()
        non_selected = bidders_name- alloted_name
        # print("NON sELECTED",non_selected)
        for non_select in non_selected:
            if non_select == "Smayra" or non_select == "Siya":
                cur.execute(f""" SELECT Bank_Bal FROM Nitesh WHERE SR_No = (SELECT MAX(SR_No) FROM Nitesh )""")
                balance = cur.fetchone()
                bank_bal= balance[0]
                bank_bal_aftr_non_allotment  = bank_bal + ipo_amt
                cur.execute(f""" UPDATE Nitesh SET Bank_Bal=? WHERE SR_No = (SELECT MAX(SR_No) FROM Nitesh )""",(bank_bal_aftr_non_allotment,))
                conn.commit()



                cur.execute(f""" SELECT Demat_Hold from {non_select} WHERE SR_No = (SELECT MAX(SR_No) FROM {non_select})""")
                balance = cur.fetchone()
                hold_amount = balance[0]
                child_new_hold_amount = hold_amount - ipo_amt
                cur.execute(f""" UPDATE {non_select} SET  Allotment_Status = 'No' WHERE IPO_Name=? """,(self.ipo,))
                cur.execute(f""" UPDATE {non_select} SET Demat_Hold = ? WHERE SR_No = (SELECT MAX(SR_No) FROM {non_select} )""",(child_new_hold_amount,))
                conn.commit()
                

            else:
                cur.execute(f""" SELECT  Bank_Bal,Demat_Hold from {non_select} WHERE SR_No = (SELECT MAX(SR_No) FROM {non_select})""")
                balance = cur.fetchone()
                bank_bal = balance[0]
                hold_amount = balance[1]
                bank_bal_aftr_non_allotment = bank_bal + ipo_amt
                hold_amount_aftr_non_allotment = hold_amount - ipo_amt
                cur.execute(f""" UPDATE {non_select} SET  Allotment_Status = 'No' WHERE IPO_Name=? """,(self.ipo,))
                cur.execute(f""" UPDATE {non_select} SET Bank_Bal=?, Demat_Hold = ? WHERE SR_No = (SELECT MAX(SR_No) FROM {non_select} )""",(bank_bal_aftr_non_allotment,hold_amount_aftr_non_allotment))
                conn.commit()
        conn.commit()
        conn.close()
        self.success_msg()
    
    
    def success_msg(self):
            
        content = MDBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10,
            md_bg_color="#DADCC3"
            
        )

        message = MDLabel(
            text="Allotment Updated Successfully!",
            bold=True
        )

        button_box = MDBoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=50,
            md_bg_color="#DADCC3"
        )

        back_btn = MDButton(
            MDButtonText(text="BACK")
        )

        button_box.add_widget(back_btn)

        content.add_widget(message)
        content.add_widget(button_box)

        self.success_popup = Popup(
            title="Allotment Message",
            content=content,
            size_hint=(0.45, 0.35),
            auto_dismiss=False
        )

        back_btn.bind(on_release=self.back_to_main)

        self.success_popup.open()
    def back_to_main(self, *args):
        self.success_popup.dismiss()
        self.manager.current = "main"





class IPOApp(MDApp):
    def build(self):
        bldr = Builder.load_string(KV)
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ManualUpdateScreen(name='manual_update'))
        sm.add_widget(NewIPOScreen(name='new_ipo'))
        sm.add_widget(AllotScreen(name='allot'))
        return sm  

IPOApp().run()