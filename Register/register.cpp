#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

void login();
void registration();
void  forgot();
void deleteUser();

int main(){

    int c;
    cout<<"\t\t\t__________________________________________________________________\n\n\n";
    cout<<"\t\t\t______________________Welcome to login Page____________\n\n\n";
    cout<<"\t\t\t_________________            MENU        ____________\n\n";
    cout<<"\t\t\t                                                      \n\n";

    cout<<"\t | Press 1 to Login                     |"<<endl;
    cout<<"\t | Press 2 to Register                  |"<<endl;
    cout<<"\t | Press 3 to forgot Password           |"<<endl;
    cout<<"\t | Press 4 to Delete your account       |"<<endl;
    cout<<"\t | Press 5 to Exit                      |"<<endl;


    cout<<"\n\t\t Please enter a number: ";
    cin>>c;
    cout<<endl;

    switch(c){

        case 1:
             login();
             break;
        case 2:
             registration();
             break;
    
        case 3:
            forgot();
            break;
        case 4:
            deleteUser();
            break;
        case 5:
            cout<<"\t\t\t  Thank you \n\n";
            break;
        default:
            system("cls");
            cout<<"\t\t\t  Enter an valid number 1 to 4  \n"<<endl;
            main();
        
    
    }

}

void login(){
    int count;
    string userId, password,id,pass;
    system("cls");
    cout<<"\t\t\t Please enter the username and password : "<<endl;
    cout<<"\t\t\t Username: ";
    cin>>userId;
    cout<<"\t\t\t Password: ";
    cin>>password;

    ifstream input("records.txt");

    while(input>>id>>pass){
        if(id==userId && pass==password){
            count=1;
            system("cls");
        }
    }
    input.close();
    
    if(count==1){
        cout<<userId<<"\n Login succesful \n";
        main();
    }
    else{
        cout<<"\n Login error please check username and password \n";

    }


}
void registration(){
    string ruserId, rpassword,rid,rpass;
    system("cls");
    cout<<"\t\t\t Username: ";
    cin>>ruserId;
    cout<<"\t\t\t Password: ";
    cin>>rpassword;

    ofstream f1("records.txt", ios::app);

    f1<<ruserId<<' '<<rpassword<<endl;
    system("cls");
    cout<<"\n\t\t\t Succesfully registered  \n";
    main();




}

void forgot(){
    int option;
    system("cls");
    cout<<"\t\t\t  You forgot yhe password ? No woories \n";
    cout<<"Press 1 to search your id by username"<<endl;
    cout<<"Press 2 to go back to main menu"<<endl;
    cout<<"\t\t\t Enter :";
    cin>>option;

    switch(option){
        case 1:{
            int count=0;
            string suserId,sid,spass;
            cout<<"\n\t\t Enter the username which you remembered: ";
            cin>>suserId;

            ifstream f2("records.txt");
            while(f2>>sid>>spass){
                if(sid==suserId){
                    count=1;
                }
            }
            f2.close();
            if(count==1){
                cout<<"\n\n Your account is found \n";
                cout<<"\n\n Your password is :"<<spass;
                main();

            }
            else{
                cout<<"\n\t Account not found \n";
                main();
            }
            break;


        }
        case 2:{
            main();
        }
        default: {

            cout<<"\t\t\t Wrong choice , Try again "<<endl;
            forgot();

        }

    }


}


void deleteUser() {
    string username;
    int count=0;
    cout<<"\n\t\t Enter your username to Delete:";
    cin>>username;
    cout<<endl;
    string tempFile = "temp.txt";
    string originalFile = "records.txt";
    string line;
    string fileUsername, filePassword;

    ifstream inFile;
    ofstream outFile;

    inFile.open(originalFile);
    outFile.open(tempFile);

    if (!inFile || !outFile) {
        cout << "Dosya acilamadi!" << endl;
        main();
    }

    while (inFile >> fileUsername >> filePassword) {
        if (!(fileUsername == username )) {
            outFile << fileUsername << ' ' << filePassword <<endl;
            count++;
        }
   
        }
    if(count>0){
        cout << "Kullanici basariyla silindi." << endl;
    }
    else{
        cout << "Kullanici bulunamadi ve silinmedi." << endl;
    }

    inFile.close();
    outFile.close();

    // Orijinal dosyayi sil ve gecici dosyayi orijinal dosya adiyla yeniden adlandir
    if (remove(originalFile.c_str()) != 0) {
    perror("Dosya silinemedi");
    }
    if (rename(tempFile.c_str(), originalFile.c_str()) != 0) {
    perror("Dosya yeniden adlandırılamadı");
    }


    main();
}
    


