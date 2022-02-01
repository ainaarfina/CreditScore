at conda cmd:

cd Documents
cd CreditScore
set FLASK_APP=run.py
set FLASK_ENV=development
set FLASK_DEBUG=1
flask run

--database
cd model
sqlite creditscore.db
.mode csv customer
.import Result.csv customer
.tables
.schema customer

<!-- <th class="text-center text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">CustomerID</th>

<form >
                    <label>Phone Number</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>

                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>

                    <label>Gender</label>
                    <div class="">
                      <input type="radio" id="male" name="gender" value="male" class="btn bg-gradient-info w-100 mt-4 mb-0"  >
                      <label for="male">Male</label>
                    
                    </div>

                    
                    <label>Plan Type</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>
                    <label>Phone</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Phone Number" aria-label="Phone Number" aria-describedby="Phone Number-addon">
                    </div>
                    <label>Age</label>
                    <div class="mb-3">
                      <input type="number" class="form-control" placeholder="Age" aria-label="Age" aria-describedby="Age-addon">
                    </div>


                    
                    <div class="text-center">
                      <button type="button" class="btn bg-gradient-info w-100 mt-4 mb-0">Predict</button>
                    </div>
                  </form>

-- inside row
<div class="col-xl-3 col-md-6 mb-xl-0 mb-4">

                

                <div class="card card-blog card-plain">
                  <!-- /// -->
                  <div class="card-body">
                    <form role="form text-left">
                      <label>Username</label>
                      <div class="mb-3">
                        <input class="form-control" placeholder="Username" aria-label="Username">
                      </div>
                      <label>Email</label>
                      <div class="mb-3">
                        <input type="email" class="form-control" placeholder="Email" aria-label="Email" aria-describedby="email-addon">
                      </div>
                      <label>Password</label>
                      <div class="mb-3">
                        <input type="password" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="password-addon">
                      </div>
                      <div class="form-check form-switch">
                        <input class="form-check-input" type="checkbox" id="rememberMe" checked="">
                        <label class="form-check-label" for="rememberMe">Terms</label>
                      </div>
                      <div class="text-center">
                        <button type="button" class="btn bg-gradient-info w-100 mt-4 mb-0">Sign UP</button>
                      </div>
                    </form>
                  </div>
                  
                  <div class="card-footer text-center pt-0 px-lg-2 px-1">
                    <p class="mb-4 text-sm mx-auto">
                      Already have an account?
                      <a href="/sign-in.html" class="text-info text-gradient font-weight-bold">Sign IN</a>
                    </p>
                  </div>
                
                </div>


              </div>