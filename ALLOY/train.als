abstract sig Station {
  station_id: one Int,
  station_code: one Int,
  station_name: one String,
  zone_id: one Int
}

abstract sig Passenger {
  login: one String,
  password: one String,
  tickets: set Ticket
}

abstract sig Train {
  train_id: one Int,
  stations: set Station,
  availability: one Int,
  classes: set TrainClass,
  schedule: one TrainSchedule,
  admin:one Admin
}

abstract sig TrainClass {
  class_id: one Int,
  class_name: one String,
  seats: set Seat
}
abstract sig Time {
  hours: one Int,
  minutes: one Int
}

abstract sig TrainSchedule {
  start_time: one Time,
  end_time: one Time,
  frequency: one String
}

abstract sig Seat {
  seat_id: one Int,
  status: one String
}

abstract sig Ticket {
  ticket_id: one Int,
  train: one Train,
  source: one Station,
  destination: one Station,
  seat: one Seat
}
abstract sig Payment {
  payment_id: one Int,
  pay_mode: one String,
  amount: one Int,
  pay_date: one Time,
  ticket: one Ticket
}

abstract sig Admin {
  login: one String,
  password: one String,
  trains: set Train,
  payments: set Payment
}
fact {
  all t: Ticket | t.source != t.destination
  all t1, t2  : Ticket | t1 != t2 implies t1.ticket_id != t2.ticket_id  // No ticket can have the same ticket_id
  all t1, t2: Ticket | t1 != t2 implies t1.source != t2.source and t1.destination != t2.destination  // No ticket can have the same source and destination
  all t1: Train | lone t1.train_id  // No train can have the same id
  all s1, s2: Station | s1 != s2 implies s1.station_id != s2.station_id and s1.station_code != s2.station_code  // No station can have the same id and code
  all p1, p2: Passenger | p1 != p2 implies p1.login != p2.login and p1.password != p2.password  // No passenger can have the same login and password
  all c1, c2: TrainClass | c1 != c2 implies c1.class_id != c2.class_id and c1.class_name != c2.class_name  // Train classes can't have the same id and name
  all p1, p2: Payment | p1 != p2 implies p1.payment_id != p2.payment_id  // Payments can't have the same id
  all t: Ticket | t.ticket_id > 0  // t Ticket IDs are positive
  all t: Train | t.train_id > 0  //Train IDs are positive
  all s: Station | s.station_id > 0 and s.station_code > 0  // t Station IDs and codes are positive
  all c: TrainClass | c.class_id > 0  //  Train Class IDs are positive
  all p: Payment | p.payment_id > 0  //  Payment IDs are positive
  all ti : Time | ti.hours > 0 
  all se: Seat | se.seat_id > 0 
}

pred BookTicket [p: Passenger, t: Train, s: Station, d: Station, c: TrainClass, se: Seat] {
  s in t.stations
  d in t.stations
  c in t.classes
  se in c.seats
  se.status = "available"
  t.availability > 0
  some ti: Ticket | ti in p.tickets and ti.train = t and ti.source = s and ti.destination = d and ti.seat = se 
}

pred CancelTicket [p: Passenger, ti: Ticket] {
  ti in p.tickets
  no ti
  ti.train.availability = ti.train.availability + 1
  ti.seat.status = "available"
}



pred ManageTrainSchedule [a: Admin, t: Train, s: TrainSchedule] {
  a in t.admin
  s = t.schedule
}

run BookTicket for 5
run CancelTicket for 5
run ManageTrainSchedule for 5
