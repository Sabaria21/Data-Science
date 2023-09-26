#!/usr/bin/env python
# coding: utf-8

# # Week 1 Review Exercises
# 

# In[ ]:


Nama : Hashimatul Zaria
NIM  : E1E121059


# Q1. Data Types
# 
# What is the data type of the variable `pop`?
# -> Apa tipe data pada variabel 'pop'?
# 
# Jawab : Tipe data pada variabel 'pop' adalah float. Tipe data float adalah tipe data yang berbentuk pecahan atau desimal.

# In[18]:


pop = 5.8
print(type(pop))


# In[ ]:


# use a suitable function to check your answer
# gunakan fungsi yang sesuai untuk memeriksa jawabanmu


# Q2. Which of the following is a valid variable name of of population below 15 years old?
# -> Mana dari berikut ini adalah nama variabel valid untuk populasi di bawah 15 tahun?
# 
# Jawab : variabel yang valid adalah "_15_below_pop = 12.33"

# In[ ]:


# which line won't give an error? Comment out the ones that do!
15_years_and_below = 12.33 #SyntaxError pada variabel ini
get_ipython().run_line_magic('_pop_15_below', '= 12.33 #SyntaxError pada variabel ini')
_15&below_pop = 12.33 #SyntaxError pada variabel ini
_15_below_pop = 12.33 #Ini adalah penulisan variabel yang benar


# In[2]:


15_years_and_below = 12.33
print(15_years_and_below)


# In[3]:


get_ipython().run_line_magic('_pop_15_below', '= 12.33')
print(%_pop_15_below)


# In[4]:


_15&below_pop = 12.33
print(_15&below_pop)


# In[5]:


_15_below_pop = 12.33 
print(_15_below_pop)


# Q3. What will be stored in `result`?
# -> Apa yang akan disimpan di dalam variabel result?
# 
# Jawab :Hasil dari variabel result = 17
# Operasi aritmatika yang digunakan:
# - + = penjumlahan
# - ** = pangkat
# - // = pembagian bulat

# In[6]:


result = 3 + 4 ** 2 - (5 // 2)
print(result)


# Q4. If Singapore has an estimated population of 5.85 million and the land area is 700 square kilometers, what is the population density (number of people per KM)? 
# 
# Jika Singapura memiliki populasi yang diperkirakan sebanyak 5.85 juta dan luas daratan adalah 700 kilometer persegi, berapa kepadatan penduduknya (jumlah orang per KM)?
# 
# Jawab : Jadi, kepadatan penduduk Singapore (jumlah orang per KM) adalah = 8357.142857142857 jiwa

# In[41]:


# Estimated total Population of Singapore, in millions 5.85
total_pop_millions = 5.85*10**6

# Total land area, in KM
land_area = 700

# How many people are there per KM?
population_density  = total_pop_millions / land_area
print("Population density per square kilometer = ",population_density)


# Q5. Write a function called `pop_density()` that receives two arguments:
# Tulis sebuah fungsi bernama pop_density() yang menerima dua argumen:
# 
# 1. the population, recorded in millions, `population_mil`
# 2. the land area, in square kilometres, `land_area_sqkm`
# - 1. populasi, dicatat dalam jutaan, population_mil
# - 2. luas wilayah, dalam kilometer persegi, land_area_sqkm
# 
# The function should calculate and return the population density. 
# Fungsi tersebut harus menghitung dan mengembalikan kepadatan penduduk.

# In[42]:


# Write the function here
# Tulis fungsi di sini

def pop_density(population_mil, land_area_sqkm):
    density = population_mil / land_area_sqkm
    print("Population density = ",density)


# In[43]:


pop_density(5.85*10**6, 700)


# Q6. Call the function you have written to calculate and display the population density of Hong Kong: 7.50 million people in a land area of 1050 km squared 
# 
# Panggil fungsi yang telah Anda tulis untuk menghitung dan menampilkan kepadatan penduduk Hong Kong: 7,50 juta orang di wilayah daratan seluas 1050 km persegi.

# In[60]:


# Call the function 
# Panggil fungsi

def calculate_population_density(population, area):
    density = population / area
    return density

# Calculating the population density of Hong Kong
hk_population = 7.50*10**6  
hk_area = 1050

hk_density = calculate_population_density(hk_population, hk_area)
print(f"The population density of Hong Kong is approximately {hk_density:.2f} people per square kilometer.")


# Q7. Using the `pop_density()` function, calculate the population density of Singapore and then use comparison operators to compare the population densities of Singapore and Hong Kong.
# -> Menggunakan fungsi pop_density(), hitung kepadatan penduduk Singapura dan kemudian gunakan operator perbandingan untuk membandingkan kepadatan penduduk Singapura dan Hong Kong.
# 
# Singapore's population: 5.85 million
# Singapore's land area: 700 sq km
# -> Populasi Singapura: 5,85 juta Orang
# Luas wilayah Singapura: 700 km persegi
# 
# (Data From [Worldometers](http://worldometers.info))
# 

# In[67]:


# Function to calculate population density
# Fungsi untuk menghitung kepadatan penduduk

def calculate_population_density(population, area):
    density = population / area
    return density


# Calculating the population density of Singapore
sg_population = 5.85*10**6 
sg_area = 700 

sg_density = calculate_population_density(sg_population, sg_area)
print(f"The population density of Singapore is approximately {sg_density:.2f} people per square kilometer.")


# In[68]:


# Comparing the population density of Singapore and Hong Kong.
# Membandingkan kepadatan penduduk Singapura dan Hong Kong

if sg_density > hk_density:
    print("In terms of population density, Singapore has a higher figure compared to Hong Kong")
elif sg_density < hk_density:
    print("In terms of population density, Hong Kong has a higher figure compared to Singapore")
else:
    print("Singapore and Hong Kong have the same population density")


# Q8. Let's add another area to compare: Macao's population is 0.65 million in a land area of 30 sq km. Find out whether Singapore's population density is higher than BOTH Hong Kong and Macao.

# In[66]:


# Calculate Macao's density (use the function!)
def calculate_population_density(population, area):
    density = population / area
    return density

# Calculating the population density of Macao
mc_population = 0.65 * 10**6  
mc_area = 700 

mc_density = calculate_population_density(mc_population, mc_area)
print(f"The population density of Macao is approximately {mc_density:.2f} people per square kilometer")


# In[65]:


# Comparing the population density of Singapore, Hong Kong, and Macao.
# Membandingkan kepadatan penduduk Singapura, Hong Kong, dan Macao

if sg_density > hk_density and sg_density > mc_density:
    print("Singapore has a higher population density than both Hong Kong and Macao.")
else:
    print("Singapore does not have a higher population density than both Hong Kong and Macao.")


# Q9. Write a function called compare_density() that receives two arguments representing the population densities of two areas. The function will compare the two values and print one of the following strings:
# -> Tulis sebuah fungsi bernama compare_density() yang menerima dua argumen yang mewakili kepadatan penduduk dari dua wilayah. Fungsi ini akan membandingkan dua nilai tersebut dan mencetak salah satu dari string berikut:
# 
# - “Area 1 has higher density”
# - “Area 2 has higher density”
# - “Both areas have the same density”
#     "Area 1 memiliki kepadatan yang lebih tinggi"
#     "Area 2 memiliki kepadatan yang lebih tinggi"
#     "Kedua wilayah memiliki kepadatan yang sama"

# In[69]:


# Write the function
# Tulis fungsi

def compare_density(density1, density2):
    if density1 > density2:
        print("Area 1 has higher density")
    elif density1 < density2:
        print("Area 2 has higher density")
    else:
        print("Both areas have the same density")


# Then we can test the function by passing the values of `sg_density` and `hk_density` as arguments.

# In[70]:


compare_density(sg_density, hk_density)


# Q10. What will be the result of the following loop?
# Apa hasil dari perulangan berikut?
# 
# ```
# for year in range(2022, 2031, 2):
#     print(year)
# ```

# In[9]:


# Type in the code for the loop given above and execute to check your answer
# Ketikkan kode untuk perulangan di atas dan jalankan untuk memeriksa jawaban Anda.

for year in range(2022, 2031, 2):
    print(year)


# Q.11 Write a function projected_population() that receives three arguments:
# -> uatlah sebuah fungsi projected_population() yang menerima tiga argumen:
# 
# - Current population, in millions
# - Growth rate
# - Current year
# - Populasi saat ini, dalam jutaan
# - Tingkat pertumbuhan
# - Tahun saat ini
# 

# The function should:
# - set the projected population to the current population
# - set the projected year to the current year
# - calculate the difference between the projected population and current population
# Fungsi ini harus:
# - atur populasi proyeksi menjadi populasi saat ini
# - atur tahun proyeksi menjadi tahun saat ini
# - menghitung selisih antara populasi proyeksi dan populasi saat ini
# 
# while the difference is between -1 and 1:
# 1. print the projected year and the projected population
# 2. calculate the projected population = projected population + projected population * growth rate / 100
# 3. update the projected year 
# 4. recalculate the difference between the projected propulation and current population
# 
# -> selama selisih berada di antara -1 dan 1:
# 1. cetak tahun proyeksi dan populasi proyeksi
# 2. hitung populasi proyeksi = populasi proyeksi + populasi proyeksi * tingkat pertumbuhan / 100
# 3. perbarui tahun proyeksi
# 4. hitung ulang selisih antara populasi proyeksi dan populasi saat ini

# In[72]:


def projected_population(current_pop, growth_rate, current_year):
    # complete the function according to the guide
    projected_population = current_pop
    projected_year = current_year

    difference = projected_population - current_pop

    while -1 <= difference <= 1:
        print(f"Projected Year: {projected_year}, Projected Population: {projected_population} million")

        projected_population += projected_population * growth_rate / 100
        projected_year += 1

        difference = projected_population - current_pop


# In[73]:


# testing with Thailand
# Percobaan dengan Thailand

print("Thailand's population growth")
projected_population(current_pop = 69.8, growth_rate = 0.3, current_year = 2020)


# Q.12 Write a function called `string_info()` which takes in a string argument and returns four values:
# - the first 3 characters
# - last 3 characters
# - the number of characters in the string
# - the string with each word capitalized
# 
# Tulis sebuah fungsi bernama string_info() yang mengambil argumen berupa string dan mengembalikan empat nilai:
# - tiga karakter pertama
# - tiga karakter terakhir
# - jumlah karakter dalam string
# - string dengan setiap kata diawali huruf besar

# In[10]:


def string_info(word): 
    # complete the function
    first_three = word[:3]
    last_three = word[-3:]
    num_haracters = len(word)
    capitaliz = word.title()
    return first_three, last_three, num_haracters, capitaliz


# In[11]:


# calling the function
# Memanggil fungsi

start, end, num, title = string_info("data science")


# In[12]:


# print what's returned
# Mencetak hasil yang dikembalikan

print(string_info("data science"))


# # Congratulations! 
# 
# You have reached the end of this notebook! Hope you have been able to practice and review the fundamental concepts in Python coding and we will do more next week!
