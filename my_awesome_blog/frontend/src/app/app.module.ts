import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { NgNawahModule } from 'ng-nawah';
import { AdminContainerComponent } from './admin-container/admin-container.component';
import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { AdminLoginComponent } from './admin-login/admin-login.component';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AdminBlogNewComponent } from './admin-blog-new/admin-blog-new.component';
import { AdminBlogListComponent } from './admin-blog-list/admin-blog-list.component';
import { AdminBlogEditComponent } from './admin-blog-edit/admin-blog-edit.component';
import { AdminCommentPendingListComponent } from './admin-comment-pending-list/admin-comment-pending-list.component';


@NgModule({
	declarations: [
		AppComponent,
		HomeComponent,
		AdminContainerComponent,
		AdminLoginComponent,
		AdminDashboardComponent,
		AdminBlogNewComponent,
		AdminBlogListComponent,
		AdminBlogEditComponent,
		AdminCommentPendingListComponent
	],
	imports: [
		BrowserModule,
		AppRoutingModule,
		NgNawahModule,
		FormsModule
	],
	providers: [],
	bootstrap: [AppComponent]
})
export class AppModule { }
