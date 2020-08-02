import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';

import { NgNawahModule } from 'ng-nawah';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HomePage } from './pages/home/home.page';
import { AdminLoginPage } from './pages/admin-login/admin-login.page';
import { AdminDashboardPage } from './pages/admin-dashboard/admin-dashboard.page';
import { AdminBlogNewPage } from './pages/admin-blog-new/admin-blog-new.page';
import { AdminBlogListPage } from './pages/admin-blog-list/admin-blog-list.page';

import { AdminContainerComponent } from './shared/admin-container/admin-container.component';

@NgModule({
  declarations: [
    AppComponent,
    HomePage,
    AdminContainerComponent,
    AdminLoginPage,
    AdminDashboardPage,
    AdminBlogNewPage,
    AdminBlogListPage,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    NgNawahModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
