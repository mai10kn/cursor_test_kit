# Synthetic golden set — Login / Booking (fictional test specification)
This fixture is invented ONLY as a calibration sample, not a real project requirement.
AC-01 CONFIRMED: Password must be 8 to 20 alphanumeric characters and include at least one letter and one digit.
AC-02 CONFIRMED: After exactly 5 consecutive failed login attempts, account becomes locked.
AC-03 CONFIRMED: On successful booking cancellation, system sends a confirmation email to the booking owner.
AC-04 CONFIRMED: Owners can view only bookings for their own store; access to other stores must be denied.
AC-05 CONFIRMED: Booking date may be changed until exactly 24h before scheduled check-in; later changes are disallowed.
AC-06 CONFIRMED: A valid active user can log in with correct credentials.
No AC defines app's behavior after device network loss; do not invent a confirmed expected result.
