def booking_metrics(bookings):
    
    total = len(bookings)

    assigned = len(bookings[bookings["Status"] == "Assigned"])

    pending = len(bookings[bookings["Status"] == "Pending"])
    


    return {
        "total": total,
        "assigned": assigned,
        "pending": pending
    }