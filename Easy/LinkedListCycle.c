/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/* Ziyaret edilen düğümleri tutmak için küçük bir liste */
struct Seen {
    struct ListNode *ptr;
    struct Seen *next;
};


bool hasCycle(struct ListNode *head) {
    
    // Boş listeyi kontrol etmek
    if (head == NULL) {                               
        return false;
    }

    // Tek dgumlu listeyi kontrol etmek icin
    if (head->next == NULL) {                         
        return false;
    }

    // Tek dugumlu dongu liste
    if (head->next == head) {                      
        return true;
    }

    // Gorulen dugumleri bilgisini tutacak olan liste
    struct Seen *seen_head = NULL;

    //Verilen listeyi gezmek icin kullnacagimiz pointer
    struct ListNode *temp = head; 

    while (temp != NULL)
    {
        struct Seen *tempSeen = seen_head;

        while(tempSeen != NULL)
        {
            if(tempSeen->ptr == temp)
            {
                return true;
            }

            tempSeen = tempSeen->next;
        }

        struct Seen *node = (struct Seen *)malloc(sizeof(struct Seen));
        node->ptr = temp;
        node->next = seen_head;
        seen_head = node;

        temp = temp->next;

    }

    return false;
}