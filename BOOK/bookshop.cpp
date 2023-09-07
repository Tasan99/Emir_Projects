#include<iostream>
#include<fstream>
#include<string.h>
#include<conio.h>
#include<iomanip>

using namespace std;

class book_data{
    char books_number[30];
    char book_name[50];
    char authorname[30];
    int no_copies;


    public:
    void Get_Bookdetaıls(){
        cout<<"\nEnter detaıls your desıred book whıch you want to purchase\n";
            cout<<"\nEnter the books number:";
            cin>>books_number;
            cout<<"\nEnter the books name";
            cin.ignore();
            cin.getline(book_name,50);
            cout<<"\nEnter the authors name:";
            cin.ignore();///Hic bir parametre girilmezse sadece bir karekteri yok sayar
            cin.getline(authorname,50);/// eneter  tusuna basana kadarki - 50 sinirli
            fflush(stdin); ////tampon bellegi temizlemek  icin kullanilir (Tampon bellek kullanicinin girdigi karekterleri gecici olarak saklar)
        cout<<"\nEnter No of copies of desired book";
        cin>>no_copies;
            


        }

    void Show_book_data(){

        cout<<"\nBook Number:"<<books_number;
        cout<<"\nBook Name:"<<book_name;
        cout<<"\nAuothar Name:"<<authorname;
        cout<<"\nCopies:"<<no_copies;
        


    }

    void Modify_Book_Data(){

        cout<<"\nBook numbeer:"<<books_number;
        cout<<"/nModify the book name:";
        cin.ignore();
        cin.getline(book_name,50);
        cout<<"/nModify the authors name:";
        cin.ignore();
        cin.getline(authorname,50);
        fflush(stdin);
        cout<<"/nEnter No OF copies";
        cin>>no_copies;

    }
    char* get_book_number(){ ////Not: char* işaretçisiyle çalışırken, karakter dizisinin null karakteriyle sona erdiğinden emin olmalısınız. Aksi takdirde, belleğin sınırlarını aşarak istenmeyen sonuçlara neden olabilirsiniz.
        return books_number;
    }
    void Report(){
        cout<<books_number<<setw(30)<<book_name<<setw(30)<<authorname<<setw(30)<<no_copies<<endl;}

};

fstream fp;
book_data bk;
void write_book_data(){
    system("cls");
    int moremain;
    fp.open("book.dat",ios::out|ios::app);   ///
    do{
        bk.Get_Bookdetaıls();
        fp.write((char*)&bk,sizeof(book_data));
        cout<<"\npress 1 to add some more books to the sytem";
        cout<<"\npress 2 to go back to the main menu\n";
        cout<<"\nEnter your choice:";
        cin>>moremain;}
        while(moremain==1);
            fp.close();

}

void Display_books(char n[]){
    system("cls");
    cout<<"\nBOOK DETAILS\n";
    int check=0;
    fp.open("book.dat",ios::in);
    while(fp.read((char*)&bk,sizeof(book_data)))
    {
            if(strcmp(bk.get_book_number(),n)==0){
                bk.Show_book_data();
                check=1;
            }
    }
    fp.close();
    if(check==0){
        cout<<"\n\nBook does not exist";

    }
    getch();


}
void Modify_Book_Data(){
    
}


