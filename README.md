# Daniel Kline Code Submition 

Below is the information needed for hitting each endpoint in this code

---
I assumed element and form were the only optional data pieces in the event. And that first and last name were the only data being sent through the form.

---
I assumed the only applications sending events are 
- www.consumeraffairs.com
- www.consumeraffairs2.com
- www.consumeraffairs3.com

--- 


BASE URL = 127.0.0.1:8000/

*assuming you are using port 8000*

---


### Uploading Data:
``` json
POST eye/event/
{
  "session_id": UUID,
  "category": str,
  "name": str,
  "data": {
    "host": str,
    "path": str,
    "element": str, #optional
    "form":{ # optional
        "first_name":str,
        "last_name":str,
    }
  },
  "timestamp": datetime
}
 ```

# Getting Data

### Session ID Query 
```
GET eye/session/?session= str
```

### Category Query 
```
GET eye/category/?category= str
```

### Time Range Query 
```
GET eye/time/?timeStart=DateTimeString&timeEnd=DateTimeString
```
